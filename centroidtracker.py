# tldr >> establish box coordinates around objects, compute distance between boxes, update coordinates, register new , de-register objects that left the view

from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class CentroidTracker: 
	
# build class variables
def __init__(self, maxDisappeared=  , maxDistance=  ):
	
	# assign unique IDs to objects
	self.nextObjectID = 0
	
	# dictionary, ObjectID the key and centroid the value
	self.objects = OrderedDict()
	
	# explore the number of frames per second (fps) ObjectID has "disappeared"
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

# establish bounding box rectangles from object detector
def update(self, rects):
	
	# check if bounding box is empty
	if len(rect) == 0:
		
		# if empty, loop over ObjectIDs and mark as "disappeared"
		for objectID in list(self.disappeared.keys()):
			self.disappeared[objectID] += 1
			
			# remove given object from tracking system if marked as "missing"
			if self.disappeared[objectID] > self.maxDisappeared:
				self.deregister(objectID)
	
		# return early if no centroid or tracking info to update
		return self.objects
	
	# setup a NumPy array to store centroids for each rectangle
	inputCentroids = np.zeros((len(rects), 2), dtype="int")
	
# loop over bounding box rectangles 
for (i, (startX, startY, endX, endY)) in enumerate(rects):
	
	# compute centroid from bounding box coordinates and store it 
	cX = int((startX + endX) / 2.0)
	cY = int((startY + endY) / 2.0)
	inputCentroids[i] = (cX, cY)
	
# if not currently tracking objects, then register input centroids of new objects
if len(self.objects) == 0:
	for i in range(0, len(inputCentroids)):
		self.register(inputCentroids[i])

# otherwise,
# compute Euclidean distance between boxes and old objects with 
# distance map output array; index values with the smallest 
# corresponding distance at front of the list
else:
	
	# pull object IDs and related centroids
	objectIDs = list(self.objects.keys())
	objectCentroids = list(self.objects.values())
	
	# compute distance between object centroids and input centroids
	D = dist.cdist(np.array(objectCentroids), inputCentroids)
	
		# perform matching on rows 
	rows = D.min(axis=1).argsort()
	
		# perform matching on columns
	cols = D.argmin(axis=1)[rows]
	
	#  set up two sets to keep track of which rows and columns were previously looked at
	used Rows = set ()
	used Cols = set ()
	
	# loop over (row, column) index tuples to update object centroids
	for (row, col) in zip(rows, cols):
		
	# ignore row or column if previously looked at
		if row in usedRows or col usedCols:
			continue
	
	# if distance between centroids > maximum distance, then DO NOT associate centroids
	if D[row, col] > self.maxDistance:
		continue 
		
	# left with smallest Euclidean distances, we then pull their object IDs, 
	# and setup new centroid, plus reset our "disappeared" counter
	objectID = objectIDs[row]
	self.objects[objectID] = inputCentroids[col]
	self.disappeared[objectID] = 0
	
	# mark that we have looked at each row and column index
	usedRows.add(row)
	usedCols.add(col)
	
	# compute row and column indexing for sets we have yet to look at 
	unusedRows = set(range(0, D.shape[0])).difference(usedRows)
	unusedCols = set(range(0, D.shape[1])).difference(usedCols)
	
	# check if objects have "disappeared" or have been "lost"
	# Why? it's helpful when object centroids are greater than equal to input centroids
	if D.shape[0] >= D.shape[1]:
		
		# loop over unused row indexes
		for row in unusedRows:
		
			# pull object ID for related row and increment our "disppeared" counter
			objectID = objectIDs[row]
			self.disappeared[objectID] += 1
			
			# double check to see if marking it "disappeared" was the right move 
			if self.disappeared[objectID] > self.maxDisappeared:
				self.deregister(objectID)
		
		# otherwise, if number of input centroids > existing # of objects 
		# then loop over new centroids and register and start tracking them 		 
			for col in unusedcols:
				self.register(inputCentroids[cols])
			
	# return the set of trackable objects to calling method  
	return self.objects
