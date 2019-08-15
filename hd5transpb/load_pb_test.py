from statistics import mode
import  os
import tensorflow as tf
import numpy as np
import  cv2
from tensorflow.python.platform import gfile
pb_file_path="fer2013_mini_XCEPTION.102-0.66.pb"
jpg_path="/home/qiaocheng/PycharmProjects/face_classification-master_raspi/pic_save/167_sad.jpg"
detection_model_oath="haarcascade_frontalface_default.xml"
emotion_offsets = (20, 40)



emotion_dict= {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy',
                4: 'sad', 5: 'surprise', 6: 'neutral'}

def apply_offsets(face_coordinates, offsets):
    x, y, width, height = face_coordinates
    x_off, y_off = offsets
    return (x - x_off, x + width + x_off, y - y_off, y + height + y_off)

def detect_faces(detection_model, gray_image_array):
    return detection_model.detectMultiScale(gray_image_array, 1.3, 5)


def load_detection_model(model_path):
    detection_model = cv2.CascadeClassifier(model_path)
    return detection_model

def preprocess_input(x, v2=True):
    x = x.astype('float32')
    x = x / 255.0
    if v2:
        x = x - 0.5
        x = x * 2.0
    return x
#
#sess=tf.Session()
face_detection=load_detection_model(detection_model_oath)
f=open(pb_file_path, 'rb')
def load_model(gray_face):
    with tf.Graph().as_default():
        output_graph_def = tf.GraphDef()
        with open(pb_file_path, "rb") as f:
            output_graph_def.ParseFromString(f.read())
            tensors = tf.import_graph_def(output_graph_def, name="")
        with tf.Session() as sess:
            init = tf.global_variables_initializer()
            sess.run(init)
            op = sess.graph.get_operations()
            print("tensor:",tensors)


            for i, m in enumerate(op):
                print('op{}:'.format(i), m.values())
            input_x = sess.graph.get_tensor_by_name("input_1:0")
            print("input_x:", input_x)
            out_softmax = sess.graph.get_tensor_by_name("predictions/Softmax:0")
            print("Output:", out_softmax)
            img_out_softmax = sess.run(out_softmax, feed_dict={input_x: gray_face})
            emotion_label_arg = np.argmax(img_out_softmax)
            emotion_text = emotion_dict[emotion_label_arg]
            print("out for :", emotion_text)

sess=tf.Session()

def  model_test():
    with gfile.FastGFile(pb_file_path,'rb') as f:
        graph_def=tf.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        tf.import_graph_def(graph_def,name='')
        sess.run(tf.global_variables_initializer())
        input_x = sess.graph.get_tensor_by_name("input_1:0")
        out_softmax = sess.graph.get_tensor_by_name("predictions/Softmax:0")
        return input_x,out_softmax




def recongnize():
    #read the pic
    bgr_image=cv2.imread(jpg_path,1)
    gray_image=cv2.cvtColor(bgr_image,cv2.COLOR_BGR2GRAY)
    rgb_image=cv2.cvtColor(bgr_image,cv2.COLOR_BGR2RGB)
    faces=detect_faces(face_detection,gray_image)
    for face_coordinates in faces:
        x1,x2,y1,y2=apply_offsets(face_coordinates,emotion_offsets);
        gray_face=gray_image[y1:y2,x1:x2]
        gray_face=cv2.resize(gray_face,(64,64))
        gray_face=preprocess_input(gray_face,False)
        gray_face=np.expand_dims(gray_face,0)
        gray_face=np.expand_dims(gray_face,-1)
        #load_model(gray_face)
        #sess.run()
        input_x, out_softmax=model_test()
        img_out_softmax = sess.run(out_softmax, feed_dict={input_x: gray_face})
        emotion_label_arg = np.argmax(img_out_softmax)
        emotion_text = emotion_dict[emotion_label_arg]
        print("out for :", emotion_text)


recongnize()