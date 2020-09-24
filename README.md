*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT: Outline area around humans entering/exiting a building with a rectangle and update total number inside accordingly (See Appendix A) ***

# WHAT IS IT?

* My research extends the idea of what a neighborhood shop could be.  With the help of many other great minds I develop open source tools using the mathematical / social sciences to analyze neighborhoods shop video streams. My goal is to build computer vision models that boost classification accuracy while managing computational costs.  The hope is to showcase less costly and more social ways to perform day-to-day operations using applications of the mathematical / social sciences. 

# WHY? (SOCIAL)

* Neighborhood shops do more than provide us with essential goods. They are where unrelated people relate. They are a place you can go daily for the simple pleasure of good conversation. However, our neighborhood shops are also transforming.  They have become laboratories for new communal safety habits, much different than their orginally designed functions.  My goal is help neighborhood shops stay ahead of their competition and resolve their legacy issues now, and ensure these priceless spaces of informal public life remain engrained in our young Midwestern cities.

# WHY? (TECH)

* Visual analysis of complex neighborhood shop scenarios is an important step towards more fluid markets for humans.  Computer vision methods have shown termendous promise for scene analysis when trained on large datasets.  However, current datasets for neighborhood shop analysis are rare, and are limited to mundane environments that don't capture the complexity of the neighborhood shop.  To address this shortcoming, I present DeepNeighborhoodShop as a benchmark with a large dataset to train and test methods for several computer vision tasks.  

# HOW?

* First, I gather local knowledge (i.e. the sort that is embedded in the heads of neighborhood staff and its customers) and use it to annotate video data sets.  The data set consists of approximately ... videos collected from neighborhood shop ethnography of Chicago.  I collect and annotate the videos with comprehensive tags coming from ethnography.  These annotations enable computer vision models to learn to automatically monitor guest count, recognize their actions and understand how cues change over time to better model the temporal evolution of human actions and objects.  This benchmark serves as a testbed for future research in this challenging domain of neighborhood shop computer vision.

# NEIGHBORHOOD SHOP APPLICATIONS

* The advantage of having multiple applications for neighborhood shops is that every individual application does not have to do everything.
	* Inventory Assistant - An interface that recognizes human action data, pre-orders inventory and generates reports
	* "What You Didn't Buy" Assistant - An interface for understanding cross product interactions to better understand market segmentation and product positioning strategies
	* Autonomous Checkout - A cashier mgmt system that recognizes human action data and maintains an AR/AP, cash flow and general ledger
	
# METHODS

* Bias is inevitable when training computer vision models for human action recognition. To combat this we blend qualitative and quantitative methods to better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what humans feel is important. Our reality is political, but the dominant groups claim as the norm for building computer vision models need not be the norm.  

* STEP 1 RawData - What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, preferred work styles, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection. 
* STEP 2 TidyDataSet - How do I use ethnographic data?  I built a working auto-encoder to hone months of worth of converted ethnographic data to train computer vision models.
* STEP 3 Description - Describe each variable and values in the tidy data set
* STEP 4 ReproducibilityRecipe - Set up calculations in a way that is easy for reproducibility 
	
# SPATIAL-TEMPORAL FUSION ARCHITECTURE

* This section provides the technical contributions for fusing two models (spatial & temporal) that take advantage of pre-training on converted ethnographic data and transfer this understanding of human actions across different neighborhood shop video streams. Through a combination of mixed methods approaches, existing computer vision research, off-the-shelf hardware and human fine-tuning I create people centered applications.

* Action Classes for Neighborhood Shop Applications 
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

# WHERE TO FUSE THE 2 NETWORKS?

# IMPLEMENTATION 

# 3D CONV FUSION KERNEL

# DATA AUGMENTATION

* Sample batches of data are taken at each training cycle via corner cropping, multi-scale cropping, horizontal flips, etc.

# TESTING 

# EXPERIMENTS

# DISCUSSION 

# FUTURE RESEARCH

* Teaching machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs as real-time computer vision applications face a strict bandwidth-accuracy trade-off
* Underpinning modern tools with a public log of all queries run on video stream data to give guests better idea about how their data is used
* Restructing code and making arrays more ergonomic 
* Determining the metrics that improve downstream performance
* Lowering the costs of switching data between neighborhood shops
* Making up for the data set bias that leads to decreased generalization

* Better understanding how social, economic and legal systems work together to achieve my research goals 

# ACKNOWLEDGEMENTS

* This work was supported by my immediate family, my lovely partner K, my close friends and confidants and the open source community. 

# APPENDIX A:  PROOF-OF-CONCEPT

* Outline area around humans entering/exiting a building with a rectangle and update total number inside accordingly 

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

# APPENDIX B: POLICY MEMO

* How will the profits that accrue from increasing automation be reinvested back into communities for collective gain?

# REFERENCES

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* Deep Learning, An MIT Press Book (2016)
* The Great Good Place by Roy Oldenburg (1989)

* "The Kinetics Human Action Video Dataset" (2017)
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "MatConvNet Convolutional Neural Networks for MATLAB" (2016)
* "Spatiotemporal Residual Networks for Video Action Recognition" (2016)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Convolutional Two-Stream Network Fusion for Video Action Recognition" (2016)
* "Return of the Devil in the Details: Delving Deep into Convolutional Nets" (2014)
* "Towards Good Practices for Very Deep Two-Stream Convnets" (2015)
* "Action Recognition with Trajectory-Pooled Deep-Convolutional Descriptors" (2015)
