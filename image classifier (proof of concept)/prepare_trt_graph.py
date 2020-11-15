# import packages that define Tensorflow graphs, assist 
# in defining graphs, loading models and optimizing framework
from tensorflow.graph_util import convert_variables_to_constants
from tensorflow.graph_util import remove_training_nodes
from tensorflow.keras.models import load_model
import tensorflow.contrib.tensorrt as trt  #NVIDIA's framework
import tensorflow as tf
import argparse
import os

# freezeGraph: accepts Keras model and outputs frozen tf graph
# as a prereq to create trt graph
def freezeGraph(graph, session, outputNames):
	# start with graph's default context
	with graph.as_default():
		# remove training nodes from graph, convert graph vars to contstants
		graphDefInf = remove_training_nodes(graph.as_graph_def())
		graphDefFrozen = convert_variables_to_constants(session, 
			graphDefInf, outputNames)

		# return frozen graph
		return 

	
# command line arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-w", "--weights", required=True,
	help="path to the pretrained MobileNet V2 weights")
ap.add_argument("-t", "--trt-graph", required=True,
	help ="path to the TRT graph file")
args = vars(ap.parse_args())


# generate trt graph, fix learning rate, load model,
# extract underlying tf session
tf.keras.backend.set_learning_phase(0)
model = load_model(args["weights"]) 
session = tf.keras.backend.get_session()

# gather output names from model for layer associations
outputNames = [t.op.name for t in model.ouputs]

# start Keras-to-frozen-tf-graph conversion process
print("[INFO] freezing network...")
frozenGraph = freezeGraph(session.graph, session, outputNames)

# create trt graph from frozen tf graph using NVIDIA's trt framework
print("[INFO] creating TRT graph...")
	trtGraph = trt.create_inference_graph(
	input_graph_def=frozenGraph,
	outputs=outputNames,
	max_batch_size=1,
	max_workspace_size_bytes=1 << 25,
	precision_mode="FP16",
	minimum_segment_size=50)

# serialize trt graph to disk for inference
print("[INFO] serializing TRT graph...")
with open(args["trt_graph"], "wb") as f:
	f.write(trtGraph.SerializeToString())
