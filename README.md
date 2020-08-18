*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT ***

*** YOUTUBE DEMO ***

# INTRODUCTION

* Neighborhood shops do more than provide us with essential goods. They are a place you can go daily for the simple pleasure of good company and conversation. They are where unrelated people relate. However, these spaces of informal public life are not totally engrained in our young midwestern cities. Neighborhood shops compete with big shopping centers pulling away regulars. This research pulls together something like a work bench to preserve the social fabric of neighborhood shops and reinstate the kinds of human associations key to healthy neighborhoods. With the help of many others, I show how I'm developing a sensing system that standardizes improved methods for neighborhood shops. My research asks: are there less costly ways/more social ways to do the same tasks?

# DATA PREP: ETHNOGRAPHIC AUTOENCODER

* Neighborhood shop record systems are becoming more than mere stores of data.  The goal is to get rich ethnographic data into a coherent usable format for the sensing system. The rich data comes from neighborhood shop ethnography.  I believe new types of data help us ask new questions, new questions develop new theories and new theories create new tools.
+ So what is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, preferred work styles, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection. Next I built a working autoencoder to convert the qualitatively rich data into a usable coherent format, so it has nicer properties for the sensing system to learn good judgment.

# HOT LINE: SENSING SYSTEM 

* Through a combination of data prep, off-the-shelf hardware, cropping areas of interest, reinforcement learning, reward functions and human fine-tuning flowcharts are developed for a sensor system application. All these moving parts work together to visualize which person has what item in real-time. This approach creates an internal model of the neighborhood shop.

# MODERN TOOLS FOR NEIGHBORHOOD SHOPS

* Client Hardware: "Coffeepot" Sensing System
* Client Software: Inventory Asst, Purchasing Asst, Bookkeeping Asst
* Guest Software: "Running Tabs" Smartphone Application

# PRODUCT DESIGN

* "COFFEEPOT" - The sensors and processing power live in what looks like a coffeepot.  Its over-long body and low key placement of sensors was inspired by Josef Hoffman designs of 1904.

# PEOPLE/FOOTFALL COUNTER (PROOF-OF-CONCEPT)

01 Installing Required Packages and Libraries
* Python
* OpenCV https://opencv.org/
* dlib http://dlib.net/a

02 Configuring the Edge Computing Device (Raspberry Pi)

03 Footfall/People Counter (Plz see Attached Codebase)
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

# MODERN TOOLS FOR NEIGHBORHOOD SHOPS (FALL 2020)

01 Installing Required Packages and Libraries
* scikit-image https://scikit-image.org/
* scikit-learn https://scikit-learn.org/stable/index.html
* Numpy https://numpy.org/install/
* Keras https://keras.io/
* Tensorflow https://www.tensorflow.org
* Caffe http://caffe.berkeleyvision.org/

02 Ethnographic Autoencoder 

03 Person Detection with Tensorflow and Caffe 
* Who’s here? 

04 "Tracking People in the Wild"
* Who's here?

05 3D Hand Motion Estimation 
* Who's here?

06 Training and Deploying a Hand Motion and Item Classifier
* Whatcha up to?

07 Training and Deploying a Custom Item Classifier
* Whatcha holding?

08 Temporal Association
* Who has what item?

09 Ownership Resolution
* How do people shop? 

10 Inventory Asst 
* Planograms

11 "Running Tabs"
		
# EXPERIMENTS AND RESULTS

* Accuracy
* Computation Speed
* False Positives
* False Negatives
* False Negatives per Person
* Swaps
* Untracked People
* "Dropped Tabs"
* Model Size
* Protocols

# DISCUSSION & CHALLENGES

* How could we underpin modern tools for neighborhood shops with a public log of all queries run on video stream data?  ("thus the watchers themselves are watched")
* Teaching machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs 
* Restructing code and making arrays more ergonomic for the sensing system
* Determining the metrics that improve downstream performance
* Better understanding how social, economic and legal systems work together to achieve my research goals 

# POLICY MEMO

* How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?
* An automation tax taken on by industry and citizen could fund an independent accountability group to help communities revisit their sensing system/computer vision policies. It could help neighborhood shops and local authorities investigate public complaints regarding privacy. These recommendations are an idea in progress. At the moment I'm reading up on regulation, rules, accounting standards, community opinion and new interpretations of laws.

# BIBLIOGRAPHY

* The Great Good Place by Roy Oldenburg (1989)
* Capitalism, Socialism and Democracy by Joseph A. Schumpeter (1950)
* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* Deep Learning, An MIT Press Book by Ian Goodfellow and Yoshua Bengio and Aaron Courville (2016)
* "Fast Online Object Tracking and Segmentation: A Unifying Approach" (2019)
* "Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data" (2020)
* "Deep Reinforcement Learning from Human Preferences" (2017)
