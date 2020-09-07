*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT (Outline the area around multiple moving humans with a rectangle and count the number of humans inside a building at one time) ***

# WHAT IS IT?

* My research extends the idea of what a neighborhood shop can and should be.  With the help of other great minds, I develop open source tools using sociological methods to analyze computer vision data. My goal is to showcase less costly / more social ways to perform day-to-day shop operations using applications of the mathematical and social sciences. 

# WHY?

* Neighborhood shops do more than provide us with essential goods.  They are where unrelated people relate. They are a place you can go daily for the simple pleasure of good company and conversation.  However, these spaces of informal public life aren't totally engrained in our young Midwestern cities. I want to help neighborhood shops migrate their IT spending to the edge-cloud and stay ahead of their competition in a changing world.

# HOW?

* First, I gather local knowledge - the practical sort that is embedded in the heads of neighborhood staff, and translate it into high quality annotated video data sets.  Next, I use this information to train computer vision models to understand shoppers actions.  Finally, I feed the models video from in-store overhead cameras to track the movement of goods in neighborhood shops to real world applications.
* I believe without a deeper understanding of training data, the development of better computer vision models is reduced to costly trial-and-error. Borrowing from sociological methods like ethnography helps us better understand how our training data impacts downstream classification accuracy and build people centered applications.
 
# PEOPLE CENTERED APPLICATIONS

* Inventory Assistant via Smartphone App
* Service Notes (Autonomous Video Summarization) via Smartphone App
* Autonomous Checkout via Smartphone App
 
# PRODUCT DESIGN (PROTOTYPE)

* The sensors and processing power for the computer vision hardware live in what looks like a coffeepot.  Its over-long body and low key placement of sensors was inspired by Josef Hoffman designs of 1904.

# DATA COLLECTION & PREP

* My goal is to get neighborhood shop ethnographic data into a coherent usable format for computer vision models. I want to show how this rich data set could enable new architectures to be developed that better represent information to computer vision models.

* STEP 1 RawData - What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, preferred work styles, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection. 
* STEP 2 TidyDataSet - Build a working auto-encoder to convert the qualitatively rich data into a usable coherent format so it has nicer properties for the computer vision models.
* STEP 3 Description - Describe each variable and values in the tidy data set
* STEP 4 ReproducibilityRecipe - Set up calculations in a way that is easy for reproducibility 

* Action Classes for People Centered Applications 
	* Answering Questions
	* Bartending
	* Cleaning Floor
	* Counting Money
	* Guest Drinking
	* Guest Eating
	* Extinguishing Fire
	* Garbage Collection
	* Hugging
	* Laughing
	* Making Food
	* Making Coffee/Tea
	* Pushing Cart
	* Shaking Hands
	* Sign Language Interpreting
	* Guest Smoking
	* Using Computer
	* Sweeping Floor
	* Stocking
	* Mopping Floor
	* Water Plants
	* Petting Animals
	* Unboxing Goods
	* Sickness/Injury
	* Etc.
	
# CALCULATIONS

* Through a combination of data collection and prep, existing computer vision research, off-the-shelf hardware  and human fine-tuning I develop computer vision applications for neighborhood shops. This section provides the technical contributions for models that take advantage of pre-training on converted ethnographic data and transfer this understanding of action classes to learning across different data sets (i.e. different neighborhood shop video streams).

# PEOPLE/FOOTFALL COUNTER (PROOF-OF-CONCEPT)

* Outline the area around multiple moving humans with a rectangle and count the number of humans inside a building at one time.

01 Installing Required Packages and Libraries
* Python
* OpenCV https://opencv.org/
* dlib http://dlib.net/a

02 Configuring the Edge Computing Device (Raspberry Pi)

03 Footfall/People Counter (See Attached Codebase)
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

# REAL WORLD APPLICATIONS!

* The goal is to develop deep learning pipeines and high quality training video data sets for computer vision applications.  This section is an extension of the proof of concept.
* TLDR: Generate C/C++ code from MATLAB and deploy computer vision code to iPhone/Raspberry Pi for testing

01 Installing Required Packages and Libraries 

02 Ethnographic Autoencoder 

03 Action Recognition 

04 Implementation
		
# EXPERIMENTAL TESTS

* Mean Classification Accuracy across different architectures:

# DISCUSSION & FUTURE RESEARCH

* How could we empower guests to demand computer vision applications respect their privacy expectations?  Could we underpin modern tools with a public log of all queries run on video stream data?
* Teaching machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs as real-time computer vision applications face a strict bandwidth-accuracy trade-off
* Restructing code and making arrays more ergonomic 
* Determining the metrics that improve downstream performance
* Better capturing the relationship between time and space
* Motion stablization
* Making up for the data set bias that leads to decreased generalization
* Better understanding how social, economic and legal systems work together to achieve my research goals 

# APPENDIX: POLICY MEMO

* How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?

# REFERENCES

* The Great Good Place by Roy Oldenburg (1989)
* Capitalism, Socialism and Democracy by Joseph A. Schumpeter (1950)
* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)

* Deep Learning, An MIT Press Book (2016)
* "The Kinetics Human Action Video Dataset" (2017)
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Convolutional Two-Stream Network Fusion for Video Action Recognition" (2016)
* "MatConvNet Convolutional Neural Networks for MATLAB" (2016)
* "ImageNet Classification with Deep Convolutional Neural Networks" (2012)
* "Spatiotemporal Residual Networks for Video Action Recognition" (2016)
* "Learning Spatiotemporal Features with 3D Convolutional Neural Networks" (2015)
* "Deep Reinforcement Learning from Human Preferences" (2017)
