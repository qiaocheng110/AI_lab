from keras.models import  load_model
import  tensorflow as tf
from keras import backend as k
from tensorflow.python.framework import  graph_io
from tensorflow.python.framework.graph_util import convert_variables_to_constants


def freeze_session(session,keep_var_names=None,output_names=None,clear_devices=True):
    graph=session.graph
    with graph.as_default():
        freeze_var_names=list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names=output_names or []
        output_names +=[v.op.name for v in tf.global_variables()]
        input_graph_def=graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device=""
        frozen_graph=convert_variables_to_constants(session,input_graph_def,output_names,freeze_var_names)
        return  frozen_graph
h5_model_path='/home/qiaocheng/PycharmProjects/face_classification-master_raspi/fer2013_mini_XCEPTION.102-0.66.hdf5'
output_path='.'
pb_model_path='fer2013_mini_XCEPTION.102-0.66.pb'
k.set_learning_phase(0)
net_model=load_model(h5_model_path)

print("input is :",net_model.input.name)
print("output is :",net_model.output.name)


sess=k.get_session()
frozen_graph=freeze_session(k.get_session(),output_names=[net_model.output.op.name])
graph_io.write_graph(frozen_graph,output_path,pb_model_path,as_text=False)