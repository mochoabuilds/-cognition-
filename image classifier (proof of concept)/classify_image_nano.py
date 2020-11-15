# import packages 
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import tensorflow.contrib.tensorrt as trt
import tensorflow as tf
import numpy as np
import argparse
import time
import cv2

# load trt graph from 
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

# load our model
