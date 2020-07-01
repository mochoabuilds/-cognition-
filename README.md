*** WORKING PAPER ***

*** COMMENTS GREATLY APPRECIATED *** 

*** ATTACHED CODE IS FOR A PEOPLE/FOOTFALL COUNTER *** 

## INTRODUCTION
+ Hi there! I've long been curious about neighborhood markets (i.e. corner stores, small grocers, bodegas, farmers markets). I often ask myself, could it be simpler?  **How could we redesign the flow of checkout to render newfound benefits?** 
+ My thought is IF you were to automate checkout THEN staff would be free to: 1) chat with customers for no specific purpose 2) be the public characters that “keep an eye” on the neighborhood 3) be a “port of entry" for newcomers 4) make shopping more enjoyable and easy
+ **Through a combination of I. ethnography, II. smart contracts and III. computer vision models we paint a picture of autonomous (cashierless) checkout.**  Its algorithms, trained on data from off-the-shelf overhead cameras, sync specfic points and items in the space with connected actions such as:  walking into market, picking up items, walking out with items and upon exit a bill is calculated and sent via SMS to guests asking them to pay thru their own mobile payment system.  
 
## I. ETHNOGRAPHIC RESEARCH (TRAINING DATA)
+ What is ethnographic research? It is sociological method that uses firsthand participation in once unfamiliar social circles to pull a sense of what’s relevant in that world.  I undertook approximately 10 months of ethnographic research in two neighborhood markets to collect our training data.  **My research translates ethnographic field notes into a coherent usable format to train computer vision models.**
+ We beleive computer vision research requires a somewhat different set of tools than most scholars are currently equipped with.  They need both a deep understanding of computer vision, and they also need to understand the institutional structures of neighborhood markets.  Because of this dual complexity, collaborations with other disciplines (e.g. sociology/ethnography, law and economics) needs to be the norm. If scholars want to contribute to the great problems of the day, research must move in a cross-disciplinary direction.

## II. SMART CONTRACTS (APPROACHING DATA PRIVACY)
* We want to empower people to demand applications respect their privacy expectations, but we also don’t want to stifle innovation in the development of computer vision technology. To meet the needs of both **we underpin our computer vision application with a public log that records all events/queries run on the video stream data.**
* Our system is setup so video stream data remains in the hardware itself. Our edge-cloud software lets neighborhood market mgmt perform analysis, but only in-house, there is no copying or moving of data outside for processing. And even then, mgmt is not given free roam to pick and prod customer data. Instead we provide scripts which lets mgmt tease guest records with a log of every action they taken - “thus the watchers themselves are watched”. We want to show it's possible to create interesting computer vision applications without sweeping and invasive privacy practices.  

## III. COMPUTER VISION MODEL
+ Using translated ethnographic data we train a computer vision model to understand “whose hands are doing what, with what object” in neighborhood markets scenarios. **Our software relies on probabilities, bounding boxes and thousands of bits of feedback from human preferences to better understand which choices are closest to the desired behavior. We want our system's "reward function" to come from taking advice from humans in a collaborative process.**  Ideally our computer vision model system will gaze at the world with some empathy.

## BRINGING IT ALL TOGETHER
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

04 Footfall/People Counter Project Structure 
+ Videos
    + .avi
    + .mp4
    + .mp4
+ Output
    + .avi
+ yolo23
    + init__.py
    + centroidtracker.py
    + directioncounter.py
    + trackableobject.py
+ people_counter.py

05 Installing Required Packages and Libraries (part two)
+ scikit-image https://scikit-image.org/
+ scikit-learn https://scikit-learn.org/stable/index.html
+ Numpy https://numpy.org/install/
+ dlib http://dlib.net/
+ Keras https://keras.io/
+ Tensorflow https://www.tensorflow.org/
+ Caffe http://caffe.berkeleyvision.org/

06 Human Pose Estimation with Tensorflow and Caffe | Who’s here? 
![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)

07 Training and Deploying a Custom Gesture Recognition Model | Whatcha up to?

08 Training and Deploying a Custom Objects Classifier | Whatcha holdin?

09 Temporal Association | Who has what?

10 Action Analysis Based on Location | SMS Notification for Payment

## EXPERIMENTS AND RESULTS
+ Summary Statistics
    + Accuracy 
    + Computation Speed
    + System Requirements
    + Model Size
    + Other
+ Datasets and Protocols
+ Results

## DISCUSSION
OPEN ISSUES
+ **Show it’s possible to get interesting services without egregious and invasive privacy practices (NO FACE RECOGNITION)**
+ Better handling the 10% of "edge cases" (unusual cases that are not commmon in training data)
+ Branch object persistence models across multiple cameras
+ Better understand the front-back orientation of human limbs due to clothing, lighting, background
+ **Lower processing power bills - bridge the Edge-Cloud barrier, apprenticeship learning, etc.** 
+ Determinine the metrics that improve downstream performance

## TIMELINE
+ Winter 2018 — Spring 2020 
    + Conceptualizing, Literature Review & Ethnographic Research 
+ Summer 2020 
    + Proof-Of-Concept:  People/Footfall Counter that tracks the number of people entering/exiting a building on a Raspberry Pi
    + Alpha:  Tracking Gestures and Classifying Items in Neighborhood Market Scenarios on a NVIDIA Jetson
+ Fall 2020 
    + Beta:  Guests walk into market, pick up items, walk out with items and upon exit a bill is calculated and sent via SMS that ask guests to pay thru their own mobile payment system.  
 
## SANDBOX
+ Reliability planning: recovering gracefully from internet/power outages
+ How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?

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
+ @misc{christiano2017deep,
    title={Deep reinforcement learning from human preferences},
    author={Paul Christiano and Jan Leike and Tom B. Brown and Miljan Martic and Shane Legg and Dario Amodei},
    year={2017},
    eprint={1706.03741},
    archivePrefix={arXiv},
    primaryClass={stat.ML}
}

## APPENDIX
