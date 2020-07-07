*** WORKING PAPER ***

*** ATTACHED CODE IS FOR A PEOPLE/FOOTFALL COUNTER *** 

## INTRODUCTION
+ Hi there! I've longgg been curious about neighborhood markets (i.e. corner stores, bakeries, food stores, small pharmacies). I often ask myself, could the checkout process be simpler? My thought is, IF you automate checkout THEN staff will be free to: 1) chat with customers for no specific purpose 2) be the public characters that “keep an eye” on the neighborhood 3) be a “port of entry" for newcomers 4) operational duties
+ Through a combination of ethnography, a public log and computer vision we show easy and enjoyable autonomous checkout could be.  **The concept is beautifully simple: make checkout so easy it feels you're stealing.**  
+ Our algorithms, trained on translated ethnographic data and video stream data from off-the-shelf overhead cameras, sync specfic points and items in a space with classifications across 400+ action classes (e.g. guests walk in, guest picks up items, guest walks out with items and upon exit a bill is sent via SMS to guests asking them to pay thru their own mobile payment system).

## TIMELINE
+ Winter 2018 — Spring 2020 
    + Conceptualizing, Literature Review & Ethnographic Research 
+ Summer 2020 
    + Proof-Of-Concept:  People/Footfall Counter that tracks the number of people entering/exiting a room 
    + Alpha:  Tracking Gestures and Classifying Items in Neighborhood Market Scenarios 
+ Fall 2020 
    + Beta:  Autonomous Checkout 
    + Features:  Inventory Assistant & Purchasing Assistant
    
 ## POLICY MEMORANDUM
+ How will the profits that accrue from increasing automation be reinvested back into communities for collective gain? 
+ In a society that respects labor rights, each person would receive a cash payment equal to their share of the value of an automation-tax, taken on industry in pursuit of economic gain.  Fee proceeds called the “universal basic dividend” would go to all in that community, to each an equal amount.  **An automation-tax on robots also provides industry with an incentive to ensure sufficient re-training, especially of low skilled workers or they bear the full brunt of the automation-tax.**
+ We understand some may see the automation-tax as an innovation penalty.  Some companies may move elsewhere to avoid the tax.  Others may see the labor-intensive, redundant tasks saved by automation as a way to transform the way they do  operations, and in some ways reshape what it means to be a neighborhood market.

## I. PARTICIPANT OBSERVATION (ETHNOGRAPHY)
+ What is ethnographic research? It is sociological method of firsthand participant obsevation in once unfamiliar social circles to pull a sense of what's relevant in that world. Ethnographic data includes: sensory impressions, personal responses, insider language, questions about behaviors, neighborhood identities, jottings, etc. I undertook approximately 10 months of ethnographic data collection work in two neighborhood markets.  **I then built software/hardware for converting ethnographic field notes into training data for computer vision models.**
+ I believe training a computer vision model requires a somewhat different set of tools than most engineers are currently equipped with.  In the case of neighborhood markets, they need both a deep understanding of computer vision and the social, environmental and governance structures of each respective neighborhood market.  Because of this dual complexity, collaborations with other disciplines needs to be the norm. If computer vision engineers want to contribute to the great problems of the day, research must move in an intrinsic and interdisciplinary direction.

## II. COMPUTER VISION MODEL
+ I train a computer vision model to rely on ethnographic field notes, probabilities and thousands of bits of feedback from human to understand which choices are closest to the desired behavior.  **We want the "reward function" of our software/hardware to come from taking advice from humans in a collaborative process.** Ideally our computer vision model system will learn to gaze at the world with some empathy.  

## III. PUBLIC LOG (DATA PRIVACY)
* We want to empower people to demand computer vision applications respect their privacy expectations, but we also don’t want to stifle innovation in the development of this technology. To meet the needs of both **we underpin our computer vision applications with a public log that records all events and queries run on the video stream data.**  
* Our setup means video stream data stays on the hardware/camera itself. Our edge-cloud software lets neighborhood market staff/mgmt perform analysis, but only in-house, there is no copying or moving of data outside for processing. Even then, staff/mgmt is not given free roam to pick and prod customer data. **We provide scripts which lets staff/mgmt tease guest records with a log of every action taken, “thus the watchers themselves are watched”.** We want to show it's possible to create interesting computer vision applications without hellish privacy practices. The idea is still in its infancy.  There is plenty of room for improvement.

## IV. BRINGING IT ALL TOGETHER
01 Installing Required Packages and Libraries (part one)
+ Python
+ OpenCV https://opencv.org/
+ dlib http://dlib.net/a

02 Configuring Edge Computing Device
+ Prep
+ Code
+ Notes

03 Open CV Crash Course
+ Prep
+ Code
+ Notes

04 Footfall/People Counter Project 
+ Videos
    + .avi
    + .mp4
    + .mp4
+ Output
    + .avi
+ cognition
    + init__.py
    + centroidtracker.py
    + directioncounter.py
    + trackableobject.py
+ people_counter.py

05 Installing Required Packages and Libraries (part two)
+ scikit-image https://scikit-image.org/
+ scikit-learn https://scikit-learn.org/stable/index.html
+ Numpy https://numpy.org/install/
+ Keras https://keras.io/
+ Tensorflow https://www.tensorflow.org/
+ Caffe http://caffe.berkeleyvision.org/

06 Human Pose Estimation with Tensorflow and Caffe | Who’s here? 
![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)

07 Training and Deploying a Custom Gesture Recognition Model | Whatcha up to?

08 Training and Deploying a Custom Objects Classifier | Whatcha holdin?

09 Temporal Association | Who has what?

10 Action Analysis Based on Location | SMS Notification for Payment

## V. EXPERIMENTS AND RESULTS
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
+ Better handle the 10% of "edge cases" (unusual cases that are not common in training data)
+ Branch object persistence models across multiple cameras
+ Better understand the front-back orientation of human limbs due to clothing, lighting, background
+ **Lower processing power bills and bridge the Edge-Cloud barrier!**
+ Determine the metrics that improve downstream performance

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
