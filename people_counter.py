import cognition.directioncounter import DirectionCounter
import cognition.centroid tracker import CentroidTracker
import cognition.trackableobject import TrackableObject
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Value
from imutils.video import VideoStream
from imutils.video import FPS
import argparse  
import imutils 
import time  
import cv 2  

# recipe for video writing process
def write_video(outputPath, writeVideo, frameQueue, W, H):
  
  # set up necessary data formats and video writer object
  fourcc = cv2.VideoWriter_fourcc(*"MJPG")
 
  # set up video writer to write frames as they become avalaible 
  writer = cv2.VideoWriter(outputPath, fourcc, 30
    (W, H), True)
    
  # start infinite loop that accepts five parameters
  while writeVideo.value or not frameQueue.empty():
    
    # check if output frame is empty or not
    if not frameQueue.empty():
    
      # pull the frame from queue and write frame
      frame = frameQueue.get()
      writer.write(frame)
    
  # when video is done let go of video writer object
  writer.release()
  
  
# argument parser that accepts four command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--mode", type=str, required=True,
  choices=["horizontal", "vertical"],
  help="direction people moving thru frame")
ap.add_argument("i", "--input", type=str,
  help="path to input video file")
ap.add_argument("-o", "--output", type=str,
  help="path to output video file")
ap.add_argument("s", "--skip-frames", type=int, default=40
  # skips frames to improve efficiency              
  help="# of skip frames between detections"

                
# if video path is empty, pull a reference from webcam
if not args.get("input", False):
  
  # start a video stream              
  print("[INFO] running video stream...")      
  vs = VideoStream(usePiCamera=True).start()
  time.sleep(2.0)
                
# otherwise grab a reference from video file
else:
  print("[INFO] opening video file...")
  vs = cv2.VideoCapture(args["input"])
  
# run video writing process object with specified frame dimensions
writerProcess = None
W = None
H = None 

# run centroid tracker, then build a list to store dlib correlation trackers,
# followed by dictionary to map each object ID to trackable object
ct = CentroidTracker(maxDisappeared=15, maxDistance=100)
trackers = []
trackableObjects = {}
                
# build the directional info variable
directionInfo = None
                
# run the foreground background subtractor, 
# build the frame per second (FPS) counter
mog = cv2.bgsegm.createBackgroundSubtractorMOG()
fps = FPS().start()

# loop over frames from video steam
while True:
                
  # grab frame and index based on if webcam or video stream
  frame = vs.read()
  frame = frame[1] if args.get("input", False) else frame

  # if viewing video and no frames grabbed then end of the video has been reached
  if args["input"] is not None and frame is None:
    break

  # set the frame dimensions and run 
  # direction counter object if needed
  if W is None or H is None:
  (H, W) = frame.shape[:2]
  dc = DirectionCounter(args["mode"], H, W)

  # begin writing video to disk if needed
  if args["output"] is not None and writerProcess is None:
    # set writeVideo flag, set up frameQueue and start writerProcess
    writeVideo = Value('i', 1)
    frameQueue = Queue()
    writerProcess = Process(target=write_video, args=(
      args["output"], writeVideo, frameQueue, W, H)) 
    writerProcess.start()   
                
   # preprocess frame and apply background subtraction
   rects = []
   
   # convert frame to grayscale and smooth it out using gaussian
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   gray = cv2.GaussianBlur(gray, (5, 5), 0)       
   
   # apply background subtraction model
   mask = mog.apply(gray)
                
   # erosions are applied to break apart components and reduce noise
   # then we find and extract contours and add the bounding boxes to rects   
   erode = cv2.erode(mask, (7, 7), iterations=2)
   cnts = cv2.findContours(erode.copy(), cv2.RETR_EXTERNAL,
   cv2.CHAIN_APPROX_SIMPLE)
   cnts = imutils.grab_contours(cnts)
                
   # loop over each contour
   for c in cnts:
   # if the contour area is less than minimum area #, then ignore object
   if cv2.contourArea(c) < 2000:
     continue 
   
   # compute bounding box coordinates of contours
   (x, y, w, h) = cv2.boundingRect(c)
   (startX, startY, endX, endY) = (x, y,x+w,y+h)

    # add bounding box coordinates to rects list
    rects.append((startX, startY, endX, endY)) 
                
    # check if the people counter direction is vertical    
    if args["mode"] == "vertical":            
       
      # draw a horizontal line in the center of the frame 
      # to mark whether people are moving 'up' or 'down' across 
      # the frame once a person crosses this line
      cv2.line(frame, (W // 2, 0), (W // 2, H), (0, 255, 255), 2)
   
    else: 
      # draw a vertical line in the center of the frame 
      # to mark whether people are moving 'left' or 'right'
      # across the frame once a person crosses this line
      cv2.line(frame, (W // 2, 0), (W // 2, H), (0, 255, 255), 2)
      
    # Counting our people! use centroid tracker to link
    # old object (i.e. people) centroids with new object centroids
    objects = ct.update(rects)
                
    # loop over tracked objects
    for (objectID, centroid) in objects.items(): 
    
      # pull trackable object via object ID
      to = trackableObjects.get(objectID, None) 
      color = (0, 0, 255) 
                
      # create a new trackable object as needed
      if to is None:
         to = TrackableObject(objectID, centroid)
                
      # otherwise, trackable object used to determine direction
      else: 
         # find direction, update centroids lists
         dc.find_direction(to, centroid)
         to.centroids.append(centroid)
                
         # check if object counted or not
         if not to.counted:
            # find direction of motion of the people
            directionInfo = dc.count_object(to, centroid)
         
         # otherwise, object counted and set color to green 
         # showing it has been counted
         else: 
            color = (0, 255, 0)
                
         # store trackable object in dictionary 
         trackableObject[objectID] = to
                
         # draw ID of object and centroid of object on output frame 
         cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
         cv2.circle(frame, (centroid[0], centroid[1]), 4, color, -1)
         
      # extract people counts and write/draw them
      if directionInfo is not None:#
        for (i, (k, v)) in enumerate(directionInfo):
          text = "{}: {}".format(k, v)
          cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
       
    # finish out loop ...
                
