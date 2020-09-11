*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT - Outline area around multiple moving people with a rectangle and count the total number of people inside a building at one time (See Appendix B) ***

# WHAT IS IT?

* My research extends the idea of what a neighborhood shop can and should be.  With the help of other great minds I develop open source tools using sociological methods to analyze computer vision data. The goal is to build networks just deep enough to boost performance while managing the cost of computational time.  My goal is to showcase my less costly / more social ways to perform day-to-day shop operations using applications of the mathematical / social sciences. 

# WHY?

* Neighborhood shops do more than provide us with essential goods.  They are where unrelated people relate. They are a place you can go daily for the simple pleasure of good company and conversation.  However, these spaces of informal public life aren't totally engrained in our young Midwestern cities. I want to help neighborhood shops migrate their IT spending to the edge-cloud and stay ahead of their competition in a changing world.

# HOW?

* First, I gather local knowledge - the practical sort that is embedded in the heads of neighborhood staff, and translate it into high quality annotated video data sets for learning hand crafed features.  Next, I use these hand crafted features to train computer vision applications to understand how cues change over time to better model the temporal evolution of actions.  I do this fusing spatial cues (i.e. action classification) and temporal cues (i.e. motion flow) so that responses at the same pixel position are put into correspondence between abstract features of the two streams. The goal is to capture actions tied to a neighborhood shop object, even as they move slightly.

* I believe without a deeper understanding of training data, the development of better computer vision models is reduced to costly trial-and-error. Borrowing from sociological methods like ethnography helps us better understand how our training data impacts downstream classification accuracy and build people centered applications.
 
# PEOPLE CENTERED APPLICATIONS

* Inventory Assistant via Smartphone App
* "Service Notes" Autonomous Video Summarization via Smartphone App
* Autonomous Checkout via Smartphone App

* Generate C/C++ code from MATLAB(MatConvNet toolbox) and deploy computer vision model to iPhone/Raspberry Pi for experiments with neighborhood shop applications

# DEEP DATA PREP

* My goal is to get neighborhood shop ethnographic data into a coherent usable format for computer vision models. I want to show how this rich data set could enable new architectures to be developed that better represent information to computer vision models.

* STEP 1 RawData - What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, preferred work styles, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection. 
* STEP 2 TidyDataSet - Build a working auto-encoder to convert the qualitatively rich data into a usable coherent format so it has nicer properties for the computer vision models.
* STEP 3 Description - Describe each variable and values in the tidy data set
* STEP 4 ReproducibilityRecipe - Set up calculations in a way that is easy for reproducibility 

* Action Classes for People Centered Applications 
	* Answering Questions
	* Bartending
	* Cleaning Floor
	* Register/POS
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
	
# SPATIAL-TEMPORAL FUSION ARCHITECTURE

* Through a combination of data collection and prep, existing computer vision research, off-the-shelf hardware  and human fine-tuning I develop computer vision applications for neighborhood shops. This section provides the technical contributions for fusing (2, spatial & temporal) VGG-16 models that take advantage of pre-training on converted ethnographic data and transfer this understanding of action classes to learning across different neighborhood shop video data streams.

# WHERE TO FUSE THE 2 NETWORKS?

# IMPLEMENTATION 

# 3D CONV FUSION KERNEL

* Convolutional kernel is set up via identity matricies (i.e. sum fusion).  This approach saves computational costs by using a much lower number of total parameters than other methods.  

# FINETUNING

* Sample batches of data at each training cycle with jitter crops, horizontal flips, etc.

# TESTING

# EXPERIMENTS

* Mean Classification Accuracy/Layers/Parameters across:
	* Data Set 1
	* Data Set 2
	* Handcrafted Data Set 

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

# APPENDIX A:  PROOF-OF-CONCEPT

* Outline area around multiple moving people with a rectangle and count the total number of people inside a building at one time.

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

# APPENDIX B: POLICY MEMO

* How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?

# REFERENCES

* The Great Good Place by Roy Oldenburg (1989)
* Capitalism, Socialism and Democracy by Joseph A. Schumpeter (1950)
* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)

* Deep Learning, An MIT Press Book (2016)
* "Deep Reinforcement Learning from Human Preferences" (2017)
* "The Kinetics Human Action Video Dataset" (2017)
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Convolutional Two-Stream Network Fusion for Video Action Recognition" (2016)
* "MatConvNet Convolutional Neural Networks for MATLAB" (2016)
* "Towards Good Practices for Very Deep Two-Stream Convnets" (2015)
" Action Recognition with Improved Trajectories" (2013)
