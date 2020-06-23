class TrackableObject: 
  def __init__(self, objectID, centroid):
    
    # accept an objectID and store its centroid attribute locational history
    self.objectID = objectID
    self.centroids = [centroid]
    
    # set up a boolean that determines whether object has been counted or not
    self.counted = False
    
    
    
