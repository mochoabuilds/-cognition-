Hardware and Software Improvements for a Low Cost Distributed Computer Vision Application (Ochoa et la., 2020)

*** WORKING PAPER ***

## INTRODUCTION 
* Hi there! I've long been puzzled by neighborhood markets. Especially its checkout process. Could it be simpler?  I dug deeper into the idea to discover the nature of the system. 
* First hand participation as a cashier has me hypothesizing that if you were to remove the checkout process entirely then staff will have more free time to:  1) chat with customers for no specific purpose  2) be the public characters that “keep an eye” on the neighborhood  3) be a “port of entry" for newcomers  4) perform non-cashier operations
* This paper explores how an autonomous checkout system customized to serve the needs of a community may implicitly incentivize the kind of human associations key to healthy neighborhoods and their tax coffers.  
* This paper also dives into the engineering of an autonomous checkout system. I use a mixed methods approach made up of ethnography, quick look perceptions and open source computer vision code.  This clever approach helps trim computational costs by only taking action when a person comes in contact with a specific space or object.  
* This trick means our distributed computer vision application is essentially a virtual reality controller.  It scans the room with an off-the-shelf camera to understand the scene and syncs specific points in the space with connected actions.  It all runs on a set of Python programs distributed among nodes, Mac & Linux hubs.
* Within a neighborhood market this dcvp setup lends itself to handsfree checkout.  It has the potential to change the neighborhood market in the long term.  Customers browse, built their basket and upon exit they are issued a check via SMS, allowing them to pay thru their own mobile payment accounts. 
  
RELATED WORK
*

## OUR MIXED METHODS APPROACH 
ETHNOGRAPHY
* What is ethnographic research? It is firsthand participation in once unfamiliar social circles to pull a sense of what’s relevant in that world. For the purpose of this research we frequent neighborhood markets in the Uptown and Edgewater neighborhoods of Chicago.
* Field Notes

QUICK LOOK GLANCES
* 

COMPUTER VISION 
* We train a distributed computer vision model to understand “whose hands are doing what, with what object” in neighborhood markets scenarios.  Algorithms divide images into regions, bounding boxes and probabilities to help machines understand their goal.  The model is then integrated into more abstract and analytical efforts (i.e. mixture density network) to help machines better understand the idiosyncrasies of each community's neighborhood market. 

* A. Human Pose Estimation | Who’s here? ![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)
* B. Gesture Recognition | Whatcha up to?
* C. Object Classification | Whatcha holdin?
* D. Temporal Association** | Who has what?
* E. Action Analysis Based on Location

MIXTURE DENSITY NETWORK (MDN)
* What is a mixed density network?
* Model:
* Network Architecture:
* Optimization:

DISTRIBUTED COMPUTER VISION PIPELINE 
* VideoNode <—> VideoHub <—> Librarian <—> UI/UX

* VideoNode** (Ethnography, Quick Look Glances, Computer Vision) //  parameter tuning to optimize detection 
* VideoHub (Computer Vision) //  log video and event message, acknowledge  
* Librarian (Computer Vision, MDN) // extracts features from video, creates summaries and reports 
* UI/UX //  SMS, mobile payments integration 

## BUILDING THIS COMPUTER VISION APPLICATION
01 Installing Required Packages and Libraries 
* Python
* OpenCV https://opencv.org/
 
02 Configuring Edge Computing Device
* Prep:
* Code:
* Notes:

03 Open CV Crash Course
* Prep:
* Code:
* Notes:
* Privacy Concerns:

04 Installing Required Packages and Libraries
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* Numpy https://numpy.org/install/ 
* dlib http://dlib.net/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org/
* Caffe http://caffe.berkeleyvision.org/

05 Footfall/People Counter
* Prep:
* Geometric Center Tracking Algorithm:
* Implementation:
* Deploying:
* Notes:
* Privacy Concerns:

06 Human Pose Estimation with Tensorflow and Caffe | Who’s here?

07 Training and Deploying Custom Gesture Recognition Model | Whatcha up to?

08 Training and Deploying Custom Objects Classifier | Whatcha holdin?

09 Temporal Association | Who has what?

10 Action Analysis Based on Location 

## EXPERIMENTS AND RESULTS
* Datasets and Protocols:
* Results: 

## DISCUSSION
OPEN ISSUES
* Showing it’s possible to get interesting services without invasive privacy practices.  
* Better grasping the front-back orientation of limbs due to clothing, lighting, background
* Branching object persistence models across multiple cameras
* Handling changing databases schema, data types and complex objects
* Determinining the metrics that improve downstream performance

## TIMELINE
* Winter 2018 thru Spring 2020 
   * Design & Conceputalizing
   * Footfoot/People counter 
* Summer 2020 
   * Human Pose Estimation w/ Tensorflow and Caffe
   * Sending/Receiving SMS notifications from hardware to Phone
* Fall 2020 
   * Pilot Product:  "Whose hands are doing what, with what object” w/ SMS checks upon exit

## SANDBOX
* Reliability planning:  recovering gracefully from internet/power outages 
* How will the profits that accrue from increasing automation be reinvested back for collective gain?

# BIBLIOGRAPHY
* The Great Good Place by Roy Oldenburg (1989)
* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* @InProceedings{Li_2019_CVPR, author = {Li, Chen and Lee, Gim Hee}, title = {Generating Multiple Hypotheses for 3D Human Pose Estimation With Mixture Density Network}, booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2019} } 
* Ye Q., Kim TK. (2018) Occlusion-Aware Hand Pose Estimation Using Hierarchical Mixture Density Network. In: Ferrari V., Hebert M., Sminchisescu C., Weiss Y. (eds) Computer Vision – ECCV 2018. ECCV 2018. Lecture Notes in Computer Science, vol 11214. Springer, Cham
* @inproceedings{zhou2020monocular, title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data}, author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng}, booktitle={Proceedings of the IEEE International Conference on Computer Vision}, pages={0--0}, year={2020} } 
