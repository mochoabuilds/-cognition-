*** WORKING PAPER ***

*** COMMENTS GREATLY APPRECIATED *** 

*** ATTACHED CODE IS FOR A PEOPLE/FOOTFALL COUNTER (PROOF OF CONCEPT) *** 

## INTRODUCTION
+ Hi there! I've long been curious about neighborhood markets (corner stores, small grocers, bodegas, farmers markets, etc), especially their checkout process. **I often ask myself, could checkout be simpler?  And could we re-engineer its flow to render newfound benefits?** Since the arrival of Covid-19 neighborhood markets have transformed into living labortories for new communal social habits. This spoke to my curioisties. **My goal became to use technology to re-engineer neighborhood markets for consumption that is more social, essential and sustainable.** 
+ First hand experience working in a neighborhood market had me hypothesizing IF you were to automate the checkout process THEN staff would be free to perform the kind of human associations key to healthy neighborhoods. Human associations could include: 1) chatting with customers for no specific purpose 2) being the public characters that “keep an eye” on the neighborhood 3) being a “port of entry" for newcomers 4) operational duties, etc  
+ Through a combination of ethnography, smart contracts and computer vision I paint a picture of a possible future -- autonomous checkout.  **Its algorithms, trained on data from off-the-shelf overhead cameras, syncs specfic points and items in the space with connected actions.**  Connected actions include:  entering the market, tracking people's choices and upon exit issuing people a bill via SMS that asks them to pay thru their own mobile payment system.  

## TIMELINE
+ Winter 2018 — Spring 2020 
    + Conceptualizing, Literature Review & Ethnographic Research 
+ Summer 2020 
    + **Proof-of-Concept :  People/Footfall Counter (customers per square feet of square space)**
    + Alpha :  Tracking Gestures and Classifying Items in Neighborhood Markets 
+ Fall 2020 
    + **Beta :  People enter the market, their choices are tracked and upon exit people are issued a bill via SMS that asks them to pay thru their own mobile payment system.**
    
## APPROACHING DATA PRIVACY
* We want to empower customers to demand applications respect their privacy expectations, but we also don’t want to stifle innovation in the development of computer vision technology.
* To meet the needs of both **we underpin our computer vision applications with a public log that records all events/queries run on the video stream data - “thus the watchers themselves are watched”** 
* Our system is setup so video stream data remains within a market's walls. Our software lets neighborhood market mgmt perform analysis only in-house, there is no copying or moving of data outside for processing. And even then, mgmt is not given free roam to pick and prod customer data. Instead we provide scripts which let them tease customer records with a log of every action they took - "thus the wathchers themselves are watched".  Our privacy system was designed for both research and privacy.  We want to show it's possible to create interesting computer vision applications without sweeping and invasive privacy practices. 

## OUR MIXED METHODS APPROACH
ETHNOGRAPHY
+ What is ethnographic research? It is firsthand participation in once unfamiliar social circles to pull a sense of what’s relevant in that world.  
+ I undertook approximately 10 months of ethnographic study in two neighborhood markets.  What piqued my interest in these two neighborhoods was that that markets layouts/human associations were organized very differently, despite the fact they shared similar economic and demographic characteristics.  I believe the best technology is not worth much without understanding the right social, environmental and governance for each marketplace.
+ Field Notes:  Data was/is gathered weekly as field notes...

QUICK LOOK GLANCES
+ What are quick look glances?  
+ Notes:  

COMPUTER VISION
+ Algorithms divide images into regions, bounding boxes and probabilities that are then integrated into more abstract and analytical efforts (i.e. mixture density networks) to help the system understand the local realities that make things work elsewhere but not here.  **The goal is to train a distributed computer vision system to understand “whose hands are doing what, with what object” in respective neighborhood markets scenarios.**

+ A. Feature Extraction - Human Pose Estimation | Who is here? ![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)
+ B. Gesture Recognition | Whatcha up to? 
+ C. Item Classification | Whatcha holdin? 
+ D. Temporal Association | Who has what? 
+ E. Action Analysis Based on Location 

## BUILDING THIS COMPUTER VISION APPLICATION
01 Installing Required Packages and Libraries (part one)
+ Python
+ OpenCV https://opencv.org/

02 Configuring Edge Computing Device
+ Prep
+ Code
+ Notes

03 Open CV Crash Course
+ Prep
+ Code
+ Notes

04 Footfall/People Counter
+ Prep
+ Geometric Center Tracking Algorithm
+ Implementation
+ SMS Notifications
+ Deploying
+ Notes
+ Privacy Concerns

04 Installing Required Packages and Libraries (part two)
+ scikit-image https://scikit-image.org/
+ scikit-learn https://scikit-learn.org/stable/index.html
+ Numpy https://numpy.org/install/
+ dlib http://dlib.net/
+ Keras https://keras.io/
+ Tensorflow https://www.tensorflow.org/
+ Caffe http://caffe.berkeleyvision.org/

06 Human Pose Estimation with Tensorflow and Caffe | Who’s here? 

07 Training and Deploying a Custom Gesture Recognition Model | Whatcha up to?

08 Training and Deploying a Custom Objects Classifier | Whatcha holdin?

**09 Temporal Association | Who has what?**

10 Action Analysis Based on Location

11 Payment via SMS

## EXPERIMENTS AND RESULTS
+ Summary Statistics
+ Datasets and Protocols
+ Results

## DISCUSSION
OPEN ISSUES
+ **Show it’s possible to get interesting services without invasive privacy practices (i.e. NO FACE RECOGNITION)**
+ Better handling the 10-20% of edge cases
+ Branch object persistence models across multiple cameras
+ Better understand the front-back orientation of limbs due to clothing, lighting, background
+ Bridge the Edge-Cloud barrier 
+ Handle changing databases schema, data types and complex objects
+ Determinine the metrics that improve downstream performance

## SANDBOX
+ Reliability planning: recovering gracefully from internet/power outages
+ How will the profits that accrue from increasing automation be reinvested back for collective gains?

## BIBLIOGRAPHY
+ The Great Good Place by Roy Oldenburg (1989)
+ Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)

+ @InProceedings{Li_2019_CVPR, author = {Li, Chen and Lee, Gim Hee}, title = {Generating Multiple Hypotheses for 3D Human Pose Estimation With Mixture Density Network}, booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2019} } 
+ Ye Q., Kim TK. (2018) Occlusion-Aware Hand Pose Estimation Using Hierarchical Mixture Density Network. In: Ferrari V., Hebert M., Sminchisescu C., Weiss Y. (eds) Computer Vision – ECCV 2018. ECCV 2018. Lecture Notes in Computer Science, vol 11214. Springer, Cham
+ @inproceedings{zhou2020monocular, title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data}, author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng}, booktitle={Proceedings of the IEEE International Conference on Computer Vision}, pages={0--0}, year={2020} } 
+ @inproceedings{martinez_2017_3dbaseline,
  title={A simple yet effective baseline for 3d human pose estimation},
  author={Martinez, Julieta and Hossain, Rayat and Romero, Javier and Little, James J.},
  booktitle={ICCV},
  year={2017}
}

## APPENDIX
