Hardware and Software Improvements to a Low-Cost Computer Vision System (Ochoa et la., 2020)

** WORKING PAPER **

ABSTRACT

 INTRODUCTION

* Hi there! The goal of this paper is to teach a computer vision system “whose hands are doing what, with what object” in the natural scene properties of a neighborhood market.  
* Our mixed methods approach uses ethnographic study, quick look glances and a computer vision model to help a machine understand neighborhood market scenarios.
* Right now, we translate our mixed methods data into a mixture density network trained on neighborhood market scene data to better solve the problem of “whose hands are doing what, with what object?” 

RELATED WORK 
OUR MIXED METHODS APPROACH
* ETHNOGRAPHY
    * Prep:  Ethnographic research is firsthand participation in unfamiliar social circles to pull a sense of what’s relevant in that world.  For the purpose of this research we frequent a neighborhood market on Chicago’s Far Northside.
    * Field Notes:
* QUICK LOOK GLANCES
    * Prep:
    * Notes:
* COMPUTER VISION MODEL
    * We use convolutional neural networks (CNN) for object detection, gesture recognition and temporal associations. Algorithms divide images into regions, bounding boxes and probabilities to understand “whose hands are doing what, with what object?”.
    * A. Human Pose Estimation — Who’s here? ![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)
    * B. Gesture Recognition — Whatcha up to?
    * C. Object Classification — Whatcha holdin?
    * D. Temporal Association — Who has what?
    * E. Action Analysis Based on Location
* MIXTURE DENSITY NETWORK
    * Model:
    * Network Architecture:
    * Optimization:

ALRIGHT! LET'S BUILD THIS COMPUTER VISION SYSTEM!

01 Installing Required Packages and Libraries 

For PART A
* Python
* OpenCV https://opencv.org/

For PART B, C & D
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* dlib http://dlib.net/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org/
* Caffe http://caffe.berkeleyvision.org/

PART A

02 Configuring Edge Computing Device
* Prep:
* Notes:

03 Open CV Crash Course
* Prep:
* Code:
* Notes:
* Privacy Concerns:

PART B

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
* *Respecting citizen privacy expectations

 DISCUSSION

GET THE TRAIN OUT THE STATION!
* We see the mass adoption of smartphones as many humans are now in arms reach of a mini-financial terminal. Our products enable businesses across the midwest to perform autonomous checkout using these mini-terminals. Our goal is to create some opportunities for new experiences around hands-free point-of-sale.  We consider the future of customer service rather than recreating old systems.  

* Spring 2020
   * Software:  Footfall/People counter
   * Hardware:  Establishing Smartphone-Hardware Communications 
* Summer 2020
   * Software:  “Whose hands are doing what, with what object?”
   * Hardware:  Extending Smartphone-Hardware Communications 
* Fall 2020
   * Software:  Autonomous Financial Services based on Temporal Association, Action Analysis, Location 
   * Hardware: 
   
SANDBOX
* How will the profits that accrue from increasing automation be redirected back into society for collective gain?

BIBLIOGRAPHY
* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011) 
* The Great Good Place by Roy Oldenburg (1989) 
* @InProceedings{Li_2019_CVPR, author = {Li, Chen and Lee, Gim Hee}, title = {Generating Multiple Hypotheses for 3D Human Pose Estimation With Mixture Density Network}, booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2019} } 
*Ye Q., Kim TK. (2018) Occlusion-Aware Hand Pose Estimation Using Hierarchical Mixture Density Network. In: Ferrari V., Hebert M., Sminchisescu C., Weiss Y. (eds) Computer Vision – ECCV 2018. ECCV 2018. Lecture Notes in Computer Science, vol 11214. Springer, Cham
* @inproceedings{wang2019fast, title={Fast online object tracking and segmentation: A unifying approach}, author={Wang, Qiang and Zhang, Li and Bertinetto, Luca and Hu, Weiming and Torr, Philip HS}, booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition}, year={2019} } 
* @inproceedings{zhou2020monocular, title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data}, author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng}, booktitle={Proceedings of the IEEE International Conference on Computer Vision}, pages={0--0}, year={2020} } 
