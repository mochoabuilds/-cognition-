Hardware and Software Improvements to a Low-Cost Computer Vision System (Ochoa et la., 2020)

** WORKING PAPER **

## GET THE TRAIN OUT THE STATION!
* There’s a need for more fluid checkout experiences right now as a result of Covid-19. We see the mass adoption of smartphones as many are now in arms reach of a mini-cash register.  Our products enable neighborhood markets to perform autonomous checkout using smartphones.  Our product gives staff more free time for purposes such as:  1) being a “port of entry" for newcomers  2) being the public characters that “keep an eye” on the neighborhood  3) daily operations 4) bringing youth and adults together in a relaxed environment.

![LombardyMarket, Richmond VA](https://user-images.githubusercontent.com/40745550/83225135-b6815a00-a144-11ea-9fb2-12da5ce78c1d.jpg)

* This paper below shows how our autonomous checkout system implicitly incentivizes the “do for one another” human associations that are key to healthy neighborhoods and their tax coffers.

INTRODUCTION
* Hi there!  Our paper is formatted to show how we train a computer vision system to understand “whose hands are doing what, with what object” in neighborhood market scenarios.  We use a mixed methods approach consisting of: ethnographic study, quick look perceptions and a computer vision model to train a computer vision model to understand neighborhood market scenarios.  We then integrate this model into more abstract tools (i.e.  a mixture density network trained on this neighborhood market data) to build a low-cost computer vision model with specific societal applications.   

RELATED WORK & BIBLIOGRAPHY
* The Great Good Place by Roy Oldenburg (1989)

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)

@InProceedings{Li_2019_CVPR, author = {Li, Chen and Lee, Gim Hee}, title = {Generating Multiple Hypotheses for 3D Human Pose Estimation With Mixture Density Network}, booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2019} } 
Ye Q., Kim TK. (2018) Occlusion-Aware Hand Pose Estimation Using Hierarchical Mixture Density Network. In: Ferrari V., Hebert M., Sminchisescu C., Weiss Y. (eds) Computer Vision – ECCV 2018. ECCV 2018. Lecture Notes in Computer Science, vol 11214. Springer, Cham

@inproceedings{zhou2020monocular, title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data}, author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng}, booktitle={Proceedings of the IEEE International Conference on Computer Vision}, pages={0--0}, year={2020} } 

## OUR MIXED METHODS APPROACH 

ETHNOGRAPHY
* Prep:  What is ethnographic research?  It is firsthand participation in unfamiliar social circles to pull a sense of what’s relevant in that world.  For the purpose of this research we frequent neighborhood markets on Chicago’s Far Northside.
* Field Notes:

QUICK LOOK GLANCES
* Prep:
* Notes:

COMPUTER VISION 

* Prep:  We use convolutional neural networks (CNN) for object detection, gesture recognition and temporal associations. Algorithms divide images into regions, bounding boxes and probabilities to understand “whose hands are doing what, with what object?"

* A. Human Pose Estimation | Who’s here? ![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)
* B. Gesture Recognition | Whatcha up to?
* C. Object Classification | Whatcha holdin?
* D. Temporal Association | Who has what?
* E. Action Analysis Based on Location

MIXTURE DENSITY NETWORK
* Prep:  What is a mixed density network?
* Model:
* Network Architecture:
* Optimization:

## ALRIGHT!! LET'S BUILD THIS LOW COST COMPUTER VISION SYSTEM! 

01 Installing Required Packages and Libraries 

For PART A
* Python
* OpenCV https://opencv.org/

For PART B
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* dlib http://dlib.net/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org/
* Caffe http://caffe.berkeleyvision.org/

PART A RECIPE
02 Configuring Edge Computing Device
* Prep:
* Notes:

03 Open CV Crash Course
* Prep:
* Code:
* Notes:
* Privacy Concerns:

PART B RECIPE
04 Human Pose Estimation with Tensorflow and Caffe — Who’s here?
* Prep:
* Code:  
* Post-Processing:
* Notes:
* Privacy Concerns:

05 Training Custom Gesture Recognition Model — Whatcha up to?

06 Training Custom Objects Classifier — Whatcha holdin?

07 Deploying Object Classifier — Whatcha holdin?

08 Temporal Association — Who has what?

PART C RECIPE
09 Action Analysis Based on Location 

EXPERIMENTS AND RESULTS
* Datasets and Protocols:
* Results: 

OPEN ISSUES
* Navigating open source software
* Grasping the front-back orientation of limbs due to clothing, lighting, background
* Determining the metrics that improve downstream performance
* Depth ambiguity, occlusion and hand pose estimation 
* Branching object persistence models across multiple cameras
* Handling changing databases schema, data types and complex objects
* Handling the velocity of vision data across different frequencies
* Respecting citizen privacy expectations

## DISCUSSION

## PRODUCT TIMELINE 
* Spring 2020 
   * Software:  Footfall/People counter
   * Hardware:  Establishing Smartphone-Hardware Communications 
* Summer 2020
   * Software:  “Whose hands are doing wha, with what object?” in Neighborhood Market Scenarios 
   * Hardware:  Extending Smartphone-Hardware Communications 
* Fall 2020
   * Software:   Autonomous Checkout using Temporal Association and Location

SANDBOX
* How will the profits that accrue from increasing automation be redirected back into society for collective gain?
