import numpy as np 

class DirectionCounter:
  def __init__(self, directionMode, H, W):
    # set up height and width of input image
    self.H = H
    self.W = W
     
    # set up variables and counters for bottom-to-top and right-to-left movement
    self.directionMode = directionMode
    self.totalUp = 0
    self.totalDown = 0
    self.totalRight = 0
    self.totalLeft = 0
     
    # set up variable holding directional movement
    self.direction = ""
     
  def find_direction(self, to, centroid):
    # pull x-coordinate from current centroids and calculate the difference 
    # between current and averages of all previous centroids to show direction
    # (negative for left movement, postive for right)
    x = [c[0] for c in to.centroids]
    delta = centroid[0] - np.mean(x)
    
    # if negative, moving left
    if delta < 0:
      self.direction = "left"
    
    # if positive, moving right
    elif delta > 0:
      self.direction = "right"
      
  # otherwise, tracking vertical movements
