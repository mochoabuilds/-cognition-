import numpy as np 

class DirectionCounter:
  def __init__(self, directionMode, H, W):
   
    # set up height and width of input video
    self.H = H
    self.W = W
     
    # set up variables and counters for bottom-to-top and right-to-left movement
    self.directionMode = directionMode
    self.totalUp = 0
    self.totalDown = 0
    self.totalRight = 0
    self.totalLeft = 0
     
    # set up variable for directional movement
    self.direction = ""
     
  def find_direction(self, to, centroid):
    
    # check if tracking horizontal movement
    if self.directionMode == "horizontal":
      
      # pull x-coordinate from current centroids and calculate difference 
      # between current and averages of all previous centroids to show direction
      # i.e. (-) for left movement & (+) for right movement
      x = [c[0] for c in to.centroids]
      delta = centroid[0] - np.mean(x)
    
        # if (-), moving left
        if delta < 0:
        self.direction = "left"
    
        # if (+), moving right
        elif delta > 0:
        self.direction = "right"
      
    # otherwise, track vertical movements
    elif self.directionMode == "vertical":
    
      # pull y-coordinate from current centroids and calculate difference
      # between current and averages of all previous centroids to show direction
      # i.e. (-) for up movement & (+) for down movement
      v = [c[1] for c in to.centroids]
      delta = centroid[1] - np.mean(y)
    
        # if (-), moving up
        if delta < 0:
        self.direction = "up"
        
        # if (+), moving down
        elif delta > 0:
        self.direction = "down"
  
      # perform actual counting
      def count_object(self, to, centroid):
    
      # run output list
      output = []
    
    # check if directional movement is horizontal
    if self.directionMode == "horizontal":
      
      # if object is left of center and moving further left
      # then count object as moving left
      leftOfCenter = centroid[0] < self.W // 2
      if self.direction == "left" and leftOfCenter:
      self.totalLeft += 1
      to.counted = True
          
      # otherwise, if directional movement is right of center 
      # and moving further right then count object as moving right
      elif self.direction == "right" and not leftOfCenter:
      self.totalRight += 1
      to.counted = True 
        
        # build list of tuples with object counts in the right and left directions
        output = [("Left", self.totalLeft), ("Right", self.totalRight)]
      
    # otherwise, directional movement is vertical
    elif self.directionMode == "vertical":
        
      # if object above middle and moving up 
      # then count object as moving up
      aboveMiddle = centroid[1] < self.H // 2
      if self.direction == "up" and aboveMiddle:
        self.totalUp += 1
        to.counted = True
        
      # otherwise, if directional movment is below the middle
      # and moving down then count object as moving down
      elif self.direction == "down" and not aboveMiddle:
        self.totalDown += 1
        to.counted = True
          
        # build list of tuples with object counts in the up and down directions
        output =[("Up", self.totalUp), ("Down", self.totalDown)]
    
    # return output list
    return output    
