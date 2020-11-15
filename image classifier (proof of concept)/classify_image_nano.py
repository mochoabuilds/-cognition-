# import packages 
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import tensorflow.contrib.tensorrt as trt
import tensorflow as tf
import numpy as np
import argparse
import time
import cv2

# load trt graph from disk
def loadTRTGraph(graphFile):
	# open graph file
	with tf.gfile.GFile(graphFile, "rb") as f:
		# setup GraphDef class and read graph
		graphDef = tf.GraphDef()
		graphDef.ParseFromString(f.read())

	# return graph
	return graphDef

# command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--trt-graph", required=True,
	help="path to the TRT graph")
ap.add_argument("-i", "--image", required=True,
	help="path to our input image")
args = vars(ap.parse_args())

# load our model, set names of input and ouput tensors to
# tell network which operation to refer to when fed image,
# and what to output when network done with inference
inputTensorName = "input_1:0"
outputTensorName = "Logits/Softmax:0"

# create path to graph file on disk so it can be loaded into memory
print("[INFO] loading TRT graph...")
trtGraph = loadTRTGraph(args["trt_graph"])

# setup config, enable GPU, create tf session, import trt graph into session
print("[INFO] initializing TensorFlow session...")
tfConfig = tf.ConfigProto()
tfConfig.gpu_options.allow_growth = True
tfSess = tf.Session(config=tfConfig)
tf.import_graph_def(trtGraph, name="")

# gather output tensor from tf session
outputTensor = tfSess.graph.get_tensor_by_name(outputTensorName)

# load input image, perform data prep for inference
image = cv2.imread(args["image"])
output = image.copy()
