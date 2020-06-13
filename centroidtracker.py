# import packages
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class CentroidTracker: 
# build class variables
def __init__(self, maxDisappeared=  , maxDistance=  ):
	# assign unique IDs to objects
	self.nextObjectID = 0
	# dictionary - ObjectID the key and centroid the value
	self.objects = OrderedDict()
	# explore number of fps ObjectID has "disappeared"
	self.disappeared = OrderedDict()
	# breakpoint fps for ObjectId to be marked "lost"
	self.maxDisappeared = maxDisappeared
	# max distance between centroids to mark ObjectID as "disappeared"
	self.maxDistance = maxDistance

# add new objects to tracker 
def register(self, centroid):
	# assign ID to the centroid
	self.objects[self.nextObjectID] = centroid
	self.disappeared[self.nextObjectID] = 0
	self.nextObjectID += 1

def deregister(self, objectID):
	# delete ObjectId from both dictionaries
	del self.objects[objectID]
	del self.disappeared[ObjectId]

# heart of centroid tracker
