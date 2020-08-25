*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT ***

# WHAT IS IT?

* My research pulls together a "work bench" to preserve the social fabric of neighborhood shops. With the help of many others, I explore: are there less costly/more social ways to do daily tasks?

# WHY?

* Neighborhood shops do more than provide us with essential goods. They are a place you can go daily for the simple pleasure of good company and conversation. They are where unrelated people relate. However, these spaces of informal public life are not totally engrained in our young midwestern cities. My goal is to provide neighborhood shops, grocers and convenience stores with modern tools they didn't know they wanted, but suddenly can't live without.

# REAL WORLD APPLICATIONS

* Client Software: Inventory Assistant via Smartphone App
* Client Hardware: Sensing System Product Design 
* Shopper Software: Autonomous Checkout via Smartphone App

# PRODUCT DESIGN

* The sensors and processing power for the client hardware live in what looks like a coffeepot.  Its over-long body and low key placement of sensors was inspired by Josef Hoffman designs of 1904.

# DATA COLLECTION & PREP
* My goal is to get rich ethnographic data into a coherent usable format for the sensing system. The rich data comes from neighborhood shop ethnography.  I want to show how this dataset could enable new neural net architectures to be developed that include multiple streams of information.    
* So what is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, preferred work styles, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection. Next I built a working autoencoder to convert the qualitatively rich data into a usable coherent format, so it has nicer properties for the sensing system to learn good judgment.

# CALCULATIONS

* Through a combination of data prep, off-the-shelf hardware, cropping areas of interest, reinforcement learning, reward functions and human fine-tuning flowcharts are developed for a sensor system application. All these moving parts work together to visualize which person has what item in real-time. 
* This section provides the technical contributions for a computer vision architecture that has the capacity to take advantage of pre-training on converted ethnographic data and transfering this high performance action classification to different datasets (i.e. different neighborhood shops).

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

# REAL WORLD APPLICATION

01 Installing Required Packages and Libraries
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* Numpy https://numpy.org/install/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org
* Caffe http://caffe.berkeleyvision.org/
*

02 Ethnographic Autoencoder 
*

03 Action Recognition 
*
		
# EXPERIMENTAL EVALUATION 

# DISCUSSION 

* How could we underpin modern tools with a public log of all queries run on video stream data?  ("thus the watchers themselves are watched")
* Teaching machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs 
* Restructing code and making arrays more ergonomic for the sensing system
* Determining the metrics that improve downstream performance
* Better understanding how social, economic and legal systems work together to achieve my research goals 

# APPENDIX: POLICY MEMO

* How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?
* An automation tax taken on by industry and citizen could fund an independent accountability group to help communities revisit their sensing system/computer vision policies. It could help neighborhood shops and local authorities investigate public complaints regarding consumer privacy. These recommendations are an idea in progress. At the moment I'm reading up on regulation, rules, community opinion and new interpretations of laws.

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
* "Spatiotemporal Residual Networks for Video Action Recognition" (2016)

* "Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data" (2020)
* "Deep Reinforcement Learning from Human Preferences" (2017)
