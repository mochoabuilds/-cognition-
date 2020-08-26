*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT ***

# WHAT IS IT?

* My research extends the idea of what a neighborhood shop can and should be. With the help of many others, I explore: are there less costly/more social ways to do day-to-day operations in neighborhood shops?

# WHY?

* Neighborhood shops do more than provide us with essential goods. They are a place you can go daily for the simple pleasure of good company and conversation. Neighborhood shops are where unrelated people relate. However, these spaces of informal public life are not totally engrained in our yung Midwestern cities. My goal is to provide them a platform-as-a-service for enabling autonomous checkout using computer vision, overhead cameras and processing power to track and process purchases of goods.  It's a modern tool neighborhood shops didn't know they wanted, but suddenly may not be able to live without.

# REAL WORLD APPLICATIONS 

* Shop Software: Inventory Assistant via Smartphone App
* Shop Hardware: Sensing System Product Design 
* Guest Software: Autonomous Checkout via Smartphone App

# PRODUCT DESIGN

* The sensors and processing power for the shop hardware live in what looks like a coffeepot.  Its over-long body and low key placement of sensors was inspired by Josef Hoffman designs of 1904.

# DATA COLLECTION & PREP
* My goal is to get rich ethnographic data into a coherent usable format for the sensing system. The rich data comes from neighborhood shop ethnography and 100 human action classes and 100 clips (10 seconds each) per class.  I want to show how this data set could enable new architectures to be developed that include multiple streams of information.    
* STEP 1 RawData - So what is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, preferred work styles, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection. 
* STEP 2 TidyDataSet - I built a working auto-encoder to convert the qualitatively rich data into a usable coherent format, so it has nicer properties for the sensing system to learn good judgment.
* STEP 3 Description - describe each variable and values in tidy data set
* STEP 4 ReproducibilityRecipe - set up calculations in a way that is easy for reproducibility

# CALCULATIONS

* Through a combination of data prep, off-the-shelf hardware, cropping areas of interest, reinforcement learning, reward functions and human fine-tuning flowcharts are developed for a sensor system application. All these moving parts work together to visualize which person has what item in real-time. 
* This section provides the technical contributions for a computer vision architecture that has the capacity to take advantage of pre-training on converted ethnographic data, and transferring this high performance action classification to learning motion features across different data sets.

# ACTION CLASSIFIER ARCHITECTURE

* The goal here is to build computer vision architectures and purposefully difficult data sets for training real world applications.
* Backbone - Inception-v1 w/batch normalization
* More to come!  

# PEOPLE/FOOTFALL COUNTER (PROOF-OF-CONCEPT)

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

# REAL WORLD APPLICATIONS 

01 Installing Required Packages and Libraries
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* Numpy https://numpy.org/install/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org
* Caffe http://caffe.berkeleyvision.org/
*

02 How the Data Set was Built
*

02 Ethnographic Autoencoder 
*

03 Action Recognition 
*
		
# EXPERIMENTAL EVALUATION 

# DISCUSSION & FUTURE RESEARCH

* How could we empower guests to demand computer vision applications respect their privacy expectations?  Could we underpin modern tools with a public log of all queries run on video stream data?
* Teaching machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs as real-time computer vision applications face a strict bandwidth-accuracy trade-off
* Restructing code and making arrays more ergonomic 
* Determining the metrics that improve downstream performance
* Better capturing the relationship between time and space
* Motion stablization?
* Making up for the data set bias that leads to decreased generalization
* Better understanding how social, economic and legal systems work together to achieve my research goals 

# APPENDIX: POLICY MEMO

* How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?
* An automation tax taken on by industry and citizen could fund an independent accountability group to help communities revisit their computer vision policies. It could help neighborhood shops and local authorities investigate public complaints regarding consumer privacy. These recommendations are an idea in progress. At the moment I'm reading up on regulation, rules, community opinion and new interpretations of laws.

# REFERENCES

* The Great Good Place by Roy Oldenburg (1989)
* Capitalism, Socialism and Democracy by Joseph A. Schumpeter (1950)
* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* Deep Learning, An MIT Press Book by Ian Goodfellow and Yoshua Bengio and Aaron Courville (2016)

* "The Kinetics Human Action Video Dataset" (2017)
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift" (2015)
* "Recurrent Batch Normalization" (2016)
* "Learning Spatiotemporal Features with 3D Convolutional Networks" (2015)
* "Spatiotemporal Residual Networks for Video Action Recognition" (2016
* "Imagenet Large Scale Visual Recognition Challenge" (2015)

* "Deep Reinforcement Learning from Human Preferences" (2017)
