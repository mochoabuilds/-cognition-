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

# accept bounding box rectangles from object detector
def update(self, rects):
	# check if bounding box is empty
	if len(rect) == 0:
		# if empty, loop over ObjectIDs and mark as disappeared
		for objectID in list(self.disappeared.keys()):
			self.disappeared[objectID] += 1
			
			# remove given object from tracking system if marked missing
			if self.disappeared[objectID] > self.maxDisappeared:
				self.deregister(objectID)
	
		# return early if no centroid or tracking info to update
		return self.objects
	
	# initialize a NumPy array to store centroids for each rect
	inputCentroids = np.zeros((len(rects), 2), dtype="int")
	
# loop over bounding box rectangles 
for (i, (startX, startY, endX, endY)) in enumerate(rects):
	# compute the centroid from bounding box coordinates and store it 
	cX = int((startX + endX) / 2.0)
	cY = int((startY + endY) / 2.0)
	inputCentroids[i] = (cX, cY)
	
# if not currently tracking objects, then register input centroids of the new objects
if len(self.objects) == 0:
	for i in range(0, len(inputCentroids)):
		self.register(inputCentroids[i])

# otherwise,
	

	

