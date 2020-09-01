*** WORKING PAPER ***

*** ATTACHED CODE FOR (PROOF-OF-CONCEPT: Outline the area around multiple moving humans with a rectangle) ***

# WHAT IS IT?

* This research extends the idea of what a neighborhood shop can and should be. To do this, I develop a suite of open-source tools for use in neighborhood shops.  With the help of many others, I develop application-specific models using sociological methods for the analysis of computer vision data. My goal is to show that there are less costly and more social ways to do day-to-day neighborhood shop operations using applications of the mathematical sciences, with an emphasis on healthier cities.

# WHY?

* Neighborhood shops do more than provide us with essential goods.  They are where unrelated people relate. They are a place you can go daily for the simple pleasure of good company and conversation.  However, these spaces of informal public life aren't totally engrained in our young Midwestern cities. 

# HOW?

* The goal is to prepare high quality annotated video data sets that present information to computer vision architectures in an appropriate manner for action recogniton using overhead cameras to track the movement of neighborhood shop goods. I beleive without a clear understanding of how and why data works, the development of better computer vision models is reduced to trial-and-error. Borrowing from sociological methods ensures our training data sets have less bias and greater generalizability. 
 
# REAL WORLD APPLICATIONS

* Computer Vision System via Product Design (see below)
* Inventory Assistant via Smartphone App
* Autonomous Checkout via Smartphone App
 
# PRODUCT DESIGN

* The sensors and processing power for the computer vision hardware live in what looks like a coffeepot.  Its over-long body and low key placement of sensors was inspired by Josef Hoffman designs of 1904.

# DATA COLLECTION & PREP

* My goal is to get rich neighborhood shop ethnographic data into a coherent usable format for the computer vision system. The collected ethnographic data is then split into two streams (spatial and temporal) and combined by fusion methods with exisiting computer vision data sets to create 100 human action classes with 100 clips lasting 10 seconds each per class. I want to show how my rich data set could enable new architectures to be developed that better represent multiple streams of information for greater generalizability.

* Action Classes for Neighborhood Shops (Working)
	* Body Motions
	* Cleaning
	* Cooking
	* Eating & Drinking
	* Hands
	* Touching Persons/Animals
	* Using Tools
	* Being Ill/Sick/Injured
	* Misc.
	
* STEP 1 RawData - What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, preferred work styles, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection. 
* STEP 2 TidyDataSet - I built a working auto-encoder to convert the qualitatively rich data into a usable coherent format so it has nicer properties for the computer vision system.
* STEP 3 Description - Here I describe each variable and values in the tidy data set
* STEP 4 ReproducibilityRecipe - Finally I set up calculations in a way that is easy for reproducibility 

# CALCULATIONS

* Through a combination of deep data prep, off-the-shelf hardware, existing computer vision research and human fine-tuning I develop a computer vision application for neighborhood shops. All these moving parts work together to visualize which person has what item in real-time. 
* This section provides the technical contributions for a computer vision architecture that has the capacity to take advantage of pre-training on converted ethnographic data and transfer this high performance action classification to learning motion features across different data sets (i.e. video streams from different neighborhood shops)

# PEOPLE/FOOTFALL COUNTER (PROOF-OF-CONCEPT)

* Outline the area around multiple moving humans with a rectangle

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

* The goal here is to build  training data sets and computer vision architectures for real world applications.
* TLDR: Generate C/C++ code from MATLAB then deploy executable code to iPhone/Raspberry Pi for experiments

01 Installing Required Packages and Libraries 

02 Ethnographic Autoencoder 

03 Action Recognition 

04 Implementation
		
# EXPERIMENTAL EVALUATION 

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
* "Visualizing and Understanding Convolutional Networks" (2013)
* "MatConvNet Convolutional Neural Networks for MATLAB" (2016)
* "ImageNet Classification with Deep Convolutional Neural Networks" (2012)
* Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift (2015)
* "Spatiotemporal Residual Networks for Video Action Recognition" (2016)
