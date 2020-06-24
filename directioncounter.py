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
    
    # check to see if tracking horizontal movement
    if self.directionMode == "horizontal":
      
      # pull x-coordinate from current centroids and calculate difference 
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
  elif self.directionMode == "vertical":
    
    # pull y-coordinate from current centroids and calculate difference
    # between current and averages of all previous centroids to show direction
    # (negative for up, positive for down)
    v = [c[1] for c in to.centroids]
    delta = centroid[1] - np.mean(y)
    
    # if negative, moving up
    if delta < 0:
        self.direction = "up"
        
    # if positive, moving down
    elif delta > 0:
        self.direction = "down"
  
  # function that performs the actual counting
  def count_object(self, to, centroid):
    
    # run the output list
    output = []
    
    # check if directional movement is horizontal
    if self.directionMode == "horizontal":
      
      # if object left of center and moving further left, 
      # count object as moving left
      leftOfCenter = centroid[0] < self.W // 2
      if self.direction == "left" and leftOfCenter:
        self.totalLeft += 1
        to.counted = True
          
      # otherwise, if directional movement is right of center 
      # and moving further right, count object as moving right
      elif self.direction == "right" and not leftOfCenter:
        self.totalRight += 1
        to.counted = True 
        
      # build list of tuples with object counts in the right and left directions
      output = [("Left", self.totalLeft), ("Right", self.totalRight)]
      
      # otherwise, directional movement is vertical
      elif self.directionMode == "vertical":
        
        # if object above the middle and moving up, 
        # count object as moving up
        aboveMiddle = centroid[1] < self.H // 2
        if self.direction == "up" and aboveMiddle:
          self.totalUp += 1
          to.counted = True
        
        # otherwise, if directional movment is below the middle
        # and moving down, count object as moving down
        elif self.direction == "down" and not aboveMiddle:
          self.totalDown += 1
          to.counted = True
          
        # build list of tuples with object counts in the up and down directions
        output =[("Up", self.totalUp), ("Down", self.totalDown)]
    
    # return dat output list
    return output    
        
        
    
