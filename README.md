“Computer Vision for Non-STEM Majors: A Mixed Methods Approach” (Ochoa et la., 2020)

** WORKING PAPER **

OVERVIEW
* Hi there! The goal of this paper is to teach a machine “whose hands are doing what, with what object” when presented with scenes of a neighborhood market. We bring together methods from complementary disciplines to better approach this experiment.
* In Part I, we describe an ETHNOGRAPHIC STUDY showing natural scene categorization of a neighborhood market.
* In Part II, we explore HUMAN SUBJECT PERCEPTIONS when they quickly glance at a photograph of neighborhood market scenes.
* In Part III, a COMPUTER VISION MODEL categorizes the natural scene properties of a neighborhood market.
* Finally in Part IV, we explain how data in Part I, Part II and Part III represent HUMAN-COMPUTER MODEL of “gut feelings” about a neighborhood market. We convert those "gut feelings" into a bayesian hierarchal model that helps the machine understand real world scenes by asking "what’s the probability that __ is the true value given the current data?”.  

RESEARCH CONTRIBUTION
* We use clever tricks to coax enormous functionality out of edge computing devices.
* We show the importance of keeping humans in the loop throughout to ensure they can team up with autonomous computer vision systems as needed for final verification.

PART I ETHNOGRAPHIC RESEARCH
* Ethnographic research is firsthand participation in once unfamiliar social circles to pull a sense of what’s relevant in that world. For the purpose of this research we frequent corner stores (and Farmers Markets) on Chicago’s Far Northside.

PART II QUICK-LOOK GLANCES
* Kat dolorem ipsum, kat dolor sit amet consectetur adipisci velit, sed kat non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam kat voluptatem.

PART III COMPUTER VISION MODEL
* Our computer vision model uses convolutional neural networks (CNN) for object detection, gesture recognition and temporal associations. Algorithms divide images into regions, bounding boxes and probabilities to understand “whose hands are doing what, with what object?”. 
* A. Human Pose Estimation — Who’s here? 
￼![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)
* B. Gesture Recognition — Whatcha up to?
* C. Object Classification — Whatcha holdin?
* D. Temporal Association — Who has what?
* E. Action Analysis Based on Location

ALRIGHT! LET'S BUILD THIS PRODUCT!

01 Installing Required Packages and Libraries 
For PART A
* Python
* OpenCV https://opencv.org/

02 Configuring Edge Computing Device
* Kat dolorem ipsum, kat dolor sit amet consectetur adipisci velit, sed kat non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam kat voluptatem.

03 Open CV Crash Course
* Kat dolorem ipsum, kat dolor sit amet consectetur adipisci velit, sed kat non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam kat voluptatem.

01 Installing Required Packages and Libraries 
For PART B, C & D
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* dlib http://dlib.net/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org/
* Caffe http://caffe.berkeleyvision.org/

04 Human Pose Estimation with Tensorflow and Caffe — Who’s here?
* What is it?
* Pre-Trained Models
* Project Structure
* Post-Processing
* Results
* Recap

05 Training Custom Gesture Recognition Model — Whatcha up to?
* What is gesture recognition?
*

06 Training Custom Objects Classifier — Whatcha holdin?
* Gathering Neighborhood Market Dataset
* Converting Neighborhood Market Notes to CSV Format
* Generating and Testing Files
* Downloading Checkpoints and Configuration
* Editing Configuration File
* Launching, Training, Monitoring Processes
* Recap

07 Deploying Object Classifier — Whatcha holdin?
* Copying Files and Generating Graph
* Preparing Graph
* Detecting Neighborhood Market Data in Images
* Testing for Images Results
* Real-Time Neighborhood Market Data
* Testing for Real-Time Data Results
* Recap

08 Temporal Association — Who has what?

09 Thermal Imaging, etc. — Double checking computer vision model 

09 Action Analysis Based on Location (i.e. Autonomous Payment Processing, etc.)

EXPERIMENTS AND RESULTS

OPEN ISSUES
* Determining the metrics that improve downstream performance
* Navigating open source software
* Handling constant partial and full occlusions
* Branching object persistence models across multiple cameras
* Handling changing databases schema, data types and complex objects
* Handling the velocity of vision data across different frequencies
* Respecting citizen privacy expectations

DISCUSSION

**PRELIMINARY BUSINESS PLAN**

* Every day, more people rely on smartphones in their daily lives.  We see the mass adoption of smartphones as — many people are now in arms reach of a mini-terminal. Our products enables small businesses and farmers markets across the midwest to perform autonomous checkout using smartphone terminals.  We create some magic and opportunity for new experiences around the autonomous point-of-sale. 

* We don’t see as our technology as new. It has been developed and used in military, industrial and commercial markets.  It’s just the time has come for neighborhood markets. The market for our products is diverse in character and highly dependent on smartphones. Our pilot product shows the benefits to be obtained for businesses operating their own autonomous checkout system.

* Pilot Product — A single embedded computer vision machine based on Nvidia hardware, attached camera/thermal sensors, etc. The system includes a thoughtfully designed molded case, power supply and smartphone-hardware communications.  With the above configuration, humans may store data and software programs written by us.  Applications include an autonomous cashier and business manager customized to serve our clients.  It’s time we elevate the quality of customer demand and rework some financial pipes. 

* Standard Costs — 
    * Nvidia hardware  $
    * Camera           $
    * Thermal Radar.   $
    * Connectors       $
    * Power Supply     $
    * Case Assembly    $ 
    *
    
* “Get the Train Out of the Station”
    * Summer 2020
        * Software: Footfall/People Counter
        * Hardware: Laying the Foundation for Hardware
    * Fall 2020
        * Software: “Whose hands are doing what, with what object?”
        * Hardware: Smartphone-Hardware Communications 
    * Winter 2020-2021
        * Software: Autonomous Payment Processing based on Action Analysis, Temporal Association and Location 

SANDBOX
* How will the profits that accrue from increasing automation be redirected back into society for collective gain?


BIBLIOGRAPHY

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011) 

* The Great Good Place by Roy Oldenburg (1989) 

* Who's Your City by Richard Florida (2008) 

* @InProceedings{Li_2019_CVPR, author = {Li, Chen and Lee, Gim Hee}, title = {Generating Multiple Hypotheses for 3D Human Pose Estimation With Mixture Density Network}, booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2019} } 

* @inproceedings{wang2019fast, title={Fast online object tracking and segmentation: A unifying approach}, author={Wang, Qiang and Zhang, Li and Bertinetto, Luca and Hu, Weiming and Torr, Philip HS}, booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition}, year={2019} } 

* @inproceedings{zhou2020monocular, title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data}, author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng}, booktitle={Proceedings of the IEEE International Conference on Computer Vision}, pages={0--0}, year={2020} 
