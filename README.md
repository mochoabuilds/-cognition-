*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT >> Outline area around moving people with a rectangle and count their total number inside a building at one time (See Appendix A) ***

# WHAT IS IT?

* My research extends the idea of what a neighborhood shop could be.  With the help of many other great minds I build open source tools using mathematical / sociological methods to analyze computer vision data streams. The goal is to build convolutional neural networks deep enough to boost performance while managing computational costs.  My goal is to showcase less costly and more fluid ways to perform day-to-day operations using applications of the mathematical / social sciences. 

# WHY THIS?

* Neighborhood shops do more than provide us with essential goods. They are a place you can go daily for the simple pleasure of good company and conversation. They are where unrelated people relate. However, these spaces of informal public life aren't totally engrained in our young Midwestern cities. My goal is help neighborhood shops stay ahead of their competition in a changing world.

# HOW?

* First, I gather local knowledge - the practical sort that is embedded in the heads of neighborhood staff, and translate it into high quality annotated video data sets for training computer vision models.  Next, I use these hand crafted data sets to train computer vision applications to understand how cues change over time to better model the temporal evolution of human actions/features.  I do this fusing spatial cues (i.e. action classification) and temporal cues (i.e. motion flow) so that responses at the same pixel position are put into correspondence between abstract features of the two streams. The helps the model understand human actions/features tied to a neighborhood shop object, especially as they move.

* Without a deeper understanding of our data sets, the development of better computer vision models is reduced to costly trial-and-error. Borrowing from sociological methods like ethnography helps us better understand how our training data impacts downstream human action classification accuracy to build people centered applications.
 
# PEOPLE CENTERED APPLICATIONS

* Generate C/C++ code from MATLAB(MatConvNet toolbox) & handcrafted data sets for deployment to iPhone/Raspberry Pi for experiments with people centered applications
* Inventory Assistant via Smartphone App
* Autonomous Checkout via Smartphone App
* Autonomous Video Summarization ("Service Notes") via Smartphone App

# DEEP DATA PREP

* My goal is to get neighborhood shop ethnographic data into a coherent usable format for computer vision models. I want to show how this rich data set could enable new architectures to be developed that better represent information to computer vision models.

* STEP 1 RawData - What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, preferred work styles, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection. 
* STEP 2 TidyDataSet - Built a working auto-encoder to convert the qualitatively rich data into a usable coherent format so it has nicer properties for the computer vision models
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

* This section provides the technical contributions for fusing 2 (spatial & temporal) VGG-16 models that take advantage of pre-training on converted ethnographic data and transfer this understanding of human action / features to learning across different neighborhood shop video data streams. Through a combination of deep data prep, existing computer vision research, off-the-shelf hardware and human fine-tuning I churn this research into a product.

# WHERE TO FUSE THE 2 NETWORKS?

# IMPLEMENTATION 

# 3D CONV FUSION KERNEL

* A convolutional kernel is set up via identity matricies (i.e. sum fusion).  This approach saves computational costs by using a much lower number of total parameters than other methods.  

# FINETUNING

* Sample batches of data are taken at each training cycle via jitter crops, horizontal flips, etc.

# TESTING

# EXPERIMENTS

* Mean Classification Accuracy
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

# ACKNOWLEDGEMENTS

* This work was supported by my immediate family, lovely partner K, close friends and confidants and the open source community. 

# APPENDIX A:  PROOF-OF-CONCEPT

* Outline area around moving people with a rectangle and count their total number inside a building at one time.

01 Installing Required Packages and Libraries
* Python
* OpenCV https://opencv.org/
* dlib http://dlib.net/a

02 Configuring the Edge Computing Device (Raspberry Pi)

03 Footfall/People Counter (See Attached Codebase)
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

04 Discussion
*

# APPENDIX B: POLICY MEMO

* How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?

# REFERENCES

* The Great Good Place by Roy Oldenburg (1989)
* Capitalism, Socialism and Democracy by Joseph A. Schumpeter (1950)
* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)

* Deep Learning, An MIT Press Book (2016)
* "Deep Reinforcement Learning from Human Preferences" (2017)
* "The Kinetics Human Action Video Dataset" (2017)
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018
* "MatConvNet Convolutional Neural Networks for MATLAB" (2016)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Convolutional Two-Stream Network Fusion for Video Action Recognition" (2016)
* "Spatiotemporal Residual Networks for Video Action Recognition" (2016)
* "Towards Good Practices for Very Deep Two-Stream Convnets" (2015)
