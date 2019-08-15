from statistics import mode
import os
import cv2
from keras.models import load_model
import numpy as np

from datasets import get_labels
from inference import detect_faces
from inference import draw_text
from inference import draw_bounding_box
from inference import apply_offsets
from inference import load_detection_model
from preprocessor import preprocess_input
import time
import picamera
import  io
# parameters for loading data and images

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.mkdir(path)
        print("====new folder====")
        print("========ok========")
    else:
        print("----There is this folder! ----")


mkdir("pic_save")

detection_model_path = 'haarcascade_frontalface_default.xml'
emotion_model_path = 'fer2013_mini_XCEPTION.102-0.66.hdf5'
emotion_labels = get_labels('fer2013')

# hyper-parameters for bounding boxes shape
frame_window = 10
emotion_offsets = (20, 40)

# loading models
face_detection = load_detection_model(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)

# getting input model shapes for inference
emotion_target_size = emotion_classifier.input_shape[1:3]  # ???1,3 represent what
# starting lists for calculating modes
emotion_window = []

# starting video streaming
cv2.namedWindow('window_frame')
#cv2.resizeWindow('window_frame', 500, 500)
#video_capture = cv2.VideoCapture(0)
count = 0
emotion_mode = ""
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 24
    time.sleep(1)
    stream=io.BytesIO()
    for foo in camera.capture_continuous(stream,format('bgr'),use_video_port=True):
        bgr_image=np.fromstring(stream.getvalue(),dtype=np.uint8)

    #    bgr_image = video_capture.read()[1]
        #bgr_image = np.empty((480 * 640 * 3,), dtype=np.uint8)
        #camera.capture(bgr_image, format='bgr', use_video_port=True)
        bgr_image = bgr_image.reshape((480, 640, 3))
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        faces = detect_faces(face_detection, gray_image)

        for face_coordinates in faces:
            count = count + 1
            x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
            gray_face = gray_image[y1:y2, x1:x2]
            try:
                gray_face = cv2.resize(gray_face, (emotion_target_size))
            except:
                continue
            gray_face = preprocess_input(gray_face, True)  # 类似于标准化的操作(64,64)
            gray_face = np.expand_dims(gray_face, 0)  # (1,64,64)
            gray_face = np.expand_dims(gray_face, -1)  # (1,64,64,1)
            emotion_prediction = emotion_classifier.predict(gray_face)
            emotion_probability = np.max(emotion_prediction)
            emotion_label_arg = np.argmax(emotion_prediction)
            emotion_text = emotion_labels[emotion_label_arg]
            emotion_window.append(emotion_text)

            if len(emotion_window) > frame_window:
                emotion_window.pop(0)
            try:
                emotion_mode = mode(emotion_window)
            except:
                continue

            if emotion_text == 'angry':
                color = emotion_probability * np.asarray((255, 0, 0))
            elif emotion_text == 'sad':
                color = emotion_probability * np.asarray((0, 0, 255))
            elif emotion_text == 'happy':
                color = emotion_probability * np.asarray((255, 255, 0))
            elif emotion_text == 'surprise':
                color = emotion_probability * np.asarray((0, 255, 255))
            else:
                color = emotion_probability * np.asarray((0, 255, 0))

            color = color.astype(int)
            color = color.tolist()

            draw_bounding_box(face_coordinates, rgb_image, color)
            draw_text(face_coordinates, rgb_image, emotion_mode,
                      color, 0, -45, 1, 1)

        bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
        if count < 10000:
            cv2.imwrite("pic_save/%d_%s" % (count, emotion_mode) + '.jpg', bgr_image)
        cv2.imshow('window_frame', bgr_image)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
        stream.truncate()
        stream.seek(0)
print("\n [INFO] Exiting program and cleanup stuff")
#video_capture.release()
camera.close()
cv2.destroyAllWindows()
