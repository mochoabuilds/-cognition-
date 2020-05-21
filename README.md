Computer Vision for Non-STEM Majors: A Mixed Methods Approach (2020) 

** WORKING PAPER ** 

OVERVIEW

* The goal of this paper is to teach a machine “whose hand are doing what, with what object” in neighborhood market scenarios.  We get the train out of the station by writing and coding on the fly. 
* In Part I, we present an ethnographic study showing natural scene categorization of a neighborhood market.
* In Part II, we explore what human subjects perceive when they quickly glance at a photograph of a neighborhood market.
* In Part III, a computer vision model categorizes the natural scene properties of a neighborhood market.
* Finally in Part IV, we show how data complied across Part I, Part II and Part III may represent “gut feelings” about neighborhood market scenes.  Then we convert those "gut feelings" into a bayesian hierarchal model that helps our computer vision system understand neighborhood market scenarios by asking "what’s the probability that __ is the true value given the current data?".  We keep humans in the loop throughout to ensure they can team up with automation systems as needed for final verification.

RESEARCH CONTRIBUTION
* We use clever tricks to coax enormous functionality out of edge computing devices.

PART I ETHNOGRAPHIC RESEARCH
* Ethnographic research is driven by firsthand participation in unfamiliar social circles to pull a sense of what’s relevant in that world. For the purpose of our research we frequent the neighborhood markets of the Chicago Far Northside.

PART II QUICK-LOOK GLANCES
* Kat dolorem ipsum, kat dolor sit amet consectetur adipisci velit, sed kat non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam kat voluptatem.

PART III COMPUTER VISION MODEL
* Our computer vision model uses convolutional neural networks (CNN) for object detection and action recognition. Algorithms divide images into regions, bounding boxes and probabilities to understand “whose hand are doing what, with what object?”. 
A.  Who is here? // Object Tracking & Human Pose Estimation 
![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82587139-40865d00-9b5e-11ea-8dfa-6bcd8757e3ec.jpeg)
B. Whatcha up to? // Action recognition 
C. What is it? // Object classification 
D. Who has what? // Temporal association (tricky!)

OK! LET'S BUILD THIS PRODUCT!

Costing = Total Main Unit + Total Design + Total Misc + Total Assembly

01 Installing Required Packages and Libraries for PART III

For PART A
* Python 
* OpenCV https://opencv.org/

For PART B, C, D
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* dlib http://dlib.net/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org/
* Caffe http://caffe.berkeleyvision.org/

PART A
02 Configuring Edge Computing Device 
* Kat dolorem ipsum, kat dolor sit amet consectetur adipisci velit, sed kat non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam kat voluptatem.

03 Open CV 
* Kat dolorem ipsum, kat dolor sit amet consectetur adipisci velit, sed kat non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam kat voluptatem.

PART B
04 Object Tracking & Human Pose Estimation 
* What is it?
* Pre-Trained Models Avaliable 
* Project Structure
* Post-Processing
* Results
* Recap

03 How to Train Custom Objects Detectors 
* Gathering Neighborhood Market Dataset
* Connverting Notes to CSV Format
* Generating and Testing Files
* Downloading Checkpoints and Configurations
* Editing Configuration File
* Launching Training, Monitoring Processes 
* Recap

04 Deploying Object Detectors 
* Copying Files and Generating Graph
* Preparing Graph
* Detecting Neighborhood Market Data in Images
* Images Testing Results 
* Real-Time Neighborhood Market Data 
* Real-Time Testing Results 
* Recap

05 How to Train Custom Gesture Recognition Model
* What is gesture recogntion?
*
*


TESTING AND RESULTS

OPEN ISSUES
* Determining the metrics that improve downstream performance
* Navigating open source software
* Handling constant partial and full occlusions
* Branching object persistence models across multiple cameras
* Restructuring the code to Rustic
* Handling changing databases schema, data types and complex objects
* Handling the velocity of vision data across different frequencies
* Respecting citizen privacy expectations

DISCUSSION

SOCIETAL APPLICATIONS
* Every day, more people rely on smartphones to do their daily functions. Our goal is to rework the pipes channeling money at neighborhood markets. The mass adoption of smartphones means many people are now in arms reach of a mini terminal. Our product enables neighborhood markets across the midwest to perform autonomous checkout using smartphone terminals.  We want to make it possible to experience automated checkout with minimum investment of time and money.  Our goal is to help neighborhood markets stay competeitive in changing times.  

* Pilot program under development. 

BIBLIOGRAPHY

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011) 
* The Great Good Place by Roy Oldenburg (1989)
* Who's Your City by Richard Florida (2008)

@InProceedings{Li_2019_CVPR,
author = {Li, Chen and Lee, Gim Hee},
title = {Generating Multiple Hypotheses for 3D Human Pose Estimation With Mixture Density Network},
booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
month = {June},
year = {2019}
}

@inproceedings{wang2019fast,
    title={Fast online object tracking and segmentation: A unifying approach},
    author={Wang, Qiang and Zhang, Li and Bertinetto, Luca and Hu, Weiming and Torr, Philip HS},
    booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
    year={2019}
}

@inproceedings{zhou2020monocular,
  title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data},
  author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  pages={0--0},
  year={2020}
}
