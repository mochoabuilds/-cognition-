*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT ***

*** YOUTUBE LINK ***

# INTRODUCTION

* Corner stores do more than just provide us with essential goods. They are a place to kick it for the simple pleasure of good company and conversation. However, the pandemic has given us new ideas about the corner store. These ideas carry new notions of convenience. My research pulls together something like a work bench to preserve the fabric of the corner store. The focus is on making change feel like a natural extension of the existing experience. 
* With the help of many others, I design and engineer corner store software for multi-sensor data fusion, summarizing, checking priors for parallels and then making decisions. First, I translate implicit cues from ethnography and conversations with residents into a usable coherent format for teaching computer vision systems to display good judgement during unusual cases not common in training data.  I see the data prep and algorithms as a human-computer duet. I teach a machine to make trade-offs between many variables, make decisions and explain its choices in corner store scenarios.

# DATA PREP: ETHNOGRAPHY & AUTOENCODER

* The journey begins here. I get rich data sets into a coherent usable format for computer vision algorithms. The rich data used comes from corner store ethnography and conversations with residents. What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Data includes: personal responses, sensory impressions, neighborhood identities, human behaviors, jottings, etc. 
* I undertook approximately 10 months of ethnography and conversations in two Chicago corner stores for initial data collection. Next I built a working autoencoder to convert ethnographic data and conversations into a different format to make the formatting have nicer properties for computer vision algorithms.  I believe new field data helps us ask new questions about corner stores, new questions develop new theories and new theories can create new tools. 

# COMPUTER VISION ALGORITHMS

* Through a combination of data collection and prep, off-the-shelf hardware, reinforcement learning, reward functions and human feedback the machine learns to solve corner store problems. For now the machine syncs specific locations/items in a corner store with classifiers across parent-child grouping.
* Right now the system works best when humans are there to hold its hand.  Feedback from humans fine-tunes its reward function to rely more on “tone” and physical environment during unusual real world cases. The machine's symbolic approach uses converted ethnography, hierarchal categories and brute computational force to solve corner store problems.  

# TIMELINE 

* Winter 2018 — Spring 2020
   	* Literature Review & Ethnography
* Summer 2020
	* People/Footfall Counter (Proof-of-Concept)
* Fall 2020
	* Better Inventory Mgmt (Hand Motion & Item Classifier)
* Winter 2021
	* Who has what object? (Temporal Association)
	* Action Analysis Based on Location (Autonomous Checkout Pt. 1)
		
# SUMMER 2020

1 Installing Required Packages and Libraries
* Python
* OpenCV https://opencv.org/
* dlib http://dlib.net/a

2 Configuring Edge Computing Device

3 Footfall/People Counter (Attached Codebase)
* Counts the # of people entering and exiting a room
* Videos/
    * .avi
    * .mp4
    * .mp4
* Output/
	* .avi
* cognition (module)
	* init__.py
	* centroidtracker.py
	* directioncounter.py
	* trackableobject.py
* people_counter.py (driver script)

# FALL 2020 & WINTER 2021

1 Installing Required Packages and Libraries
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* Numpy https://numpy.org/install/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org
* Caffe http://caffe.berkeleyvision.org/

2 Converting Field Notes for Computer Vision Algos  (Autoencoder)

3 2D Human Pose Estimation with Tensorflow and Caffe 
* Who’s here? 

4 Feature Extraction
* Who's here?

5 3D Human Pose Estimation 
* Who's here?

6 Training and Deploying a Hand Motion and Item Classifier
* Whatcha up to?

7 Training and Deploying a Custom Item Classifier
* Whatcha holding?

8 Temporal Association
* Who has what item?

9 Action Analysis Based on Location
* Autonomous Checkout Pt. 1
		
# EXPERIMENTS AND RESULTS

* Accuracy
* Computation Speed
* System Requirements
* Model Size
* Other
* Datasets and Protocols
* Results

# DISCUSSION

# POLICY MEMO

* How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?
* An automation tax taken on by industry and citizen is neccesary.  In a society that respects labor, a community would recieve cash payment equal to their share of the value of an automation-tax to enrich community infrastructure.  These are recommendations. 
* An automation tax could also fund an independent accountability group to help communities revisit their computer vision policies. It could help communities, corner stores and local authorities investigate public complaints regarding computer vision. Both recommendations are an idea in progress. I'm reading up on regulation, rules, accounting standards, community opinion and new interpretations of laws.

# SANDBOX

* How can we teach machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971?
* Why should we underpin modern tools for corner stores with a public log of all queries run on video stream data?  ("thus the watchers themselves are watched")
* Branching object persistence models across multiple cameras
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background
* Lowering processing power bills by bridging the Edge-Cloud barrier
* Determining the metrics that improve downstream performance
* How could I better understand how social, economic and legal systems work together to achieve my research goals? 

# BIBLIOGRAPHY

* The Great Good Place by Roy Oldenburg (1989)

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)

* Deep Learning, An MIT Press Book by Ian Goodfellow and Yoshua Bengio and Aaron Courville

* "Fast Online Object Tracking and Segmentation: A Unifying Approach" (2019)

* "Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data" (2020)

* "Deep Reinforcement Learning from Human Preferences" (2017)
