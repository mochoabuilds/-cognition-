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

# swap the color channels for OpenCV ordering, and resize image for 
# MobileNet V2 classification CNN expectations
image = cv2.cvtColor(image, cv2.COLOR.BGR2RGB)
image = cv2.resize(image, (224, 224))

# add batch dimension to image for easier prediction/pre-processing 
image = np.expand_dims(image, axis=0)
image = preprocess_input(image)

# run the Jetson! pass image through TensorFlow session to gather predictions
start = time.time()
predictions = tfSess.run(outputTensor,
	feed_dict={inputTensorName: image})
end = time.time()
print("[INFO] classification took {:.4f} seconds...".format(
	end - start))

# loop over top-5 predictions
topPredictions = decode_predictions(predictions, top=5)

# loop over results
for (i, prediction) in enumerate(topPredictions[0]):
	# check if this top result, if so draw label on image
	if i == 0:
		# format image and draw prediction on output image
		label = prediction[1].upper()
 		text = "Label: {}, {:.2f}%".format(label,
			prediction[2] * 100)
		cv2.putText(output, text, (10, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
		
	# display classification result on terminal
	print("{}. {}: {:.2f}%".format(i + 1, prediction[1].upper(),
		prediction[2] * 100))
		
# show output image
cv2.imshow("Output", output)
cv2.waitKey(0)

		   
		   
		   
