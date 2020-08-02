*** WORKING PAPER ***

*** ATTACHED CODE FOR PEOPLE/FOOTFALL COUNTER (PROOF-OF-CONCEPT) ***

*** YOUTUBE VIDEO OF PEOPLE/FOOTFALL COUNTER  ***

# INTRODUCTION

* Corner stores have many roles beyond providing us essential goods. They are a place to hang out for the simple pleasure of good company and conversation.  Corner stores are inherently valuable spaces.  Unfortunately, the pandemic has given new ideas on how to occupy them. These new ideas carry new notions of law, time and social norms for corner stores. Change means both loss as well as gain.
* My research pulls together something like a work bench to preserve the fabric of the corner store and multiply its efficiency. My focus is on making change feel like a natural extension of the existing experience. With the help of many others, I design and engineer software for multi-sensor data fusion, summarizing, checking any priors for parallels and then making decisions.  We focus on computer vision expertise and implicit cues from ethnography to help machines display good judgement. This approach better avoids interference with other optical sensors, reflective objects, clothing, lighting and unconscious bias. 
* I see the research as human-computer optimization problem. I teach a machine to make trade-offs between many variables to arrive at a solution that minimizes as many variables as possible.  Then I integrate it all into modern tools for corner stores that multiply their efficiency while preserving the fabric of the space.

# LEADING QUESTIONS

* Could we underpin modern tools for corner stores with a public log of all queries run on video stream data?  ("thus the watchers themselves are watched")
* Can we teach machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971?
* How could I better understand how social, economic and legal systems work together to achieve my research goals? 

# DATA COLLECTION & PREP

* The journey begins here. I get rich data sets into a coherent usable format for computer vision algorithms. The rich data used to develop theory comes from ethnography. What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Data includes: personal responses, sensory impressions, neighborhood identities, human behaviors, jottings, etc. I undertook approximately 10 months of ethnography in two Chicago corner stores for data collection. Next I built a working autoencoder to convert ethnographic data into a different format to make the formatting have nicer properties for computer vision algorithms. 

# COMPUTER VISION ALGORITHMS

* Through a combination of data collection and prep, off-the-shelf hardware, reinforcement learning, reward functions and human feedback our machine learns to solve problems. The device syncs specific locations and items in a corner store with classifiers across parent-child grouping.
* The system works best when humans are there to hold its hand.  Feedback from humans fine-tunes its reward function to rely more on “tone” and physical environment. The machines symbolic approach uses converted ethnography, hierarchal categories and brute computational force to build modern tools for corner stores.

# TIMELINE 

* Winter 2018 — Spring 2020
   	* Literature Review & Ethnography
* Summer 2020
	* People/Footfall Counter 
* Fall 2020
	* Better Inventory Mgmt (Item Classifier & Hand Motion Classifier)
* Winter 2021
	* "Who has what object?" (Autonomous Checkout Pt. 1)
	
# SUMMER 2020

1 Installing Required Packages and Libraries
* Python
* OpenCV https://opencv.org/
* dlib http://dlib.net/a

2 Configuring Edge Computing Device
* Prep
* Notes
* Code

3 Footfall/People Counter | Counts the # of people entering and exiting a room
* Prep
* Notes

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

2 Converting Ethnography Field Notes for CV Algorithms
* At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.

3 2D Human Pose Estimation with Tensorflow and Caffe
* Who’s here? 

4 Feature Extraction
* Who's here?

5 3D Human Pose Estimation
* Who's here?

6 Training and Deploying a Hand Motion and Object Classifier
* Whatcha up to?

7 Training and Deploying a Custom Objects Classifier
* Whatcha holding?

8 Temporal Association
* Who has what object?

9 Action Analysis Based on Location
* Autonomous Checkout Pt. 1

# EXPERIMENTS AND RESULTS

Summary Statistics
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
* An Automation-Tax taken on industry is necessary. We anticipate opposition. These are merely recommendations. In a society that respects labor rights, each community would receive a cash payment equal to their share of the value of an automation-tax.  Fee proceeds called the “automation-dividend” would go the community for dispersal.  
* A tax could also fund an independent accountability group to help communities revisit their computer vision policy. It could help communities, corner stores and local authorities investigate public complaints regarding computer vision.
* This is all an idea in progress. I'm reading up on regulation, rules, accounting standards, community opinion and new interpretations of laws.

# SANDBOX

* Show it’s possible to get interesting services without egregious and invasive privacy practices (NO BIOMETRICS)
* Better handling the 10% of "edge cases" (unusual cases that are not common in training data)
* Branching object persistence models across multiple cameras
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background
* Lower processing power bills by bridging the Edge-Cloud barrier
* Determine the metrics that improve downstream performance

# BIBLIOGRAPHY

* The Great Good Place by Roy Oldenburg (1989)

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)

* Deep Learning, An MIT Press Book by Ian Goodfellow and Yoshua Bengio and Aaron Courville

* "Fast Online Object Tracking and Segmentation: A Unifying Approach" (2019)

* "Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data" (2020)

* "Deep Reinforcement Learning from Human Preferences" (2017)
