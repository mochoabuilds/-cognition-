*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT: Plz See Appendix A) ***

# WHAT IS IT?

* My research extends the idea of what a neighborhood shop could be.  With the help of many other great minds I develop open source tools using the mathematical & social sciences to analyze neighborhood shop video streams, and build a computer vision applications that have high classification accuracy while managing computational costs.  The hope is to showcase less costly and more social ways to perform day-to-day shop operations using applications of the mathematical & social sciences. 

# WHY? (SOCIAL REASONS)

* Neighborhood shops do more than provide us with essential goods. They are where unrelated people relate. They are a place you can go daily for the simple pleasure of good conversation. However, our neighborhood shops are also transforming.  They have become laboratories for new communal safety habits, much different than their orginally designed functions.  My goal is help neighborhood shops maintain control of their digital infrastructure, such as hardware that runs their key mobile apps, and ensure these valuable spaces of informal public life remain engrained in our young Midwestern cities.

# WHY? (TECH REASONS)

* Visual analysis of complex neighborhood shop scenarios is an important step towards more fluid markets for humans.  Computer vision methods have shown termendous promise for scene analysis when trained on large datasets.  However, current datasets for neighborhood shop analysis are rare, and are limited to mundane environments that don't capture the complexity of the neighborhood shop.  To address this shortcoming, I present DeepNeighborhoodShop as a benchmark with a large dataset to train and test classification accuracy across human action classes. 

# RELATED WORKS

# HOW? (TLDR)

* A whole new commercial machine was created to build these computer vision application. First, I gathered local knowledge (i.e. the sort that is embedded in the heads of neighborhood staff and its customers) and used it to annotate video data sets.  The data set consists of numerous video clips collected during my years long ethnography of neighborhood shops. I then annotate specific human action classes in video with comprehensive tags.  These annotations enable computer vision machines learn to recognize human actions and understand how cues change over time to better understand the temporal evolution in neighborhood shop scenarios.  

# NEIGHBORHOOD SHOP APPLICATIONS

* "Sometimes long-term simplicity is achieved only through bursts of complexity that rework current systems." 

* This section shows how we're creating new tools for the neighborhood shop that enable seamless inventory counts, sales, etc.
	* 01_Inventory Assistant >> An interface that recognizes human action data, pre-orders inventory, generates reports
	* 02_"What You Didn't Buy" Assistant >> An interface for understanding cross product interactions to better understand market segmentation and product positioning strategies
	* 03_Autonomous Checkout >> A cashier mgmt system that recognizes human action data and maintains guest shopping carts, an AR/AP, cash flow and general ledger
	
# A. METHODS (DATA PREP)

* Bias is inevitable when training computer vision models for human action recognition. To combat this we blend qualitative and quantitative methods to better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what humans feel is important. Our reality is political, but the dominant groups claim as the norm for building computer vision models need not be the dominant view.  Our data prep hones years worth of ethnographic data on neighborhood shops into data used to a computer vision machine.

* STEP 1 RawData >> What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world (i.e. preferences, values, beliefs). Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, etc. I embarked on 10 months of ethnography in two Chicago neighborhood shops for data collection, and I've also observed my immediate and extended family run neighborhood shops across a variety of industries.
* STEP 2 TidyDataSet >> In-house Autonencoder
* STEP 3 ReproducibilityRecipe >> Set up calculations in a way that is easy for reproducibility 
	
# B. ARCHITECTURE PROPOSED FOR BOTH STREAMS 

* This section provides the technical contributions for fusing two convolutional nets (spatial & temporal). The detector (i.e. spatial net) detects high motion regions and captures the static cues as the shape and color of objects related to actions.  Whereas the "desciptior" (i.e. temporal model) describes what is happening in high motion regions. Next we use a deep architecture to encode deep learned representations into the "descriptors" to recognize human action classes in raw unseen neighborhood shop video with high accuracy.

* Action recognition in video's challenges: low video resolution (224 x 224), learning complex motion patterns and styles, background clutter, high dimensionality of video data and small datasets for training very deep models.  To address this challenge we pretrain 2 streams (spatial & temporal) on a ResNet50 net trained on ImageNet data. We then decouple the streams to pretrain spatial net on ImageNet, as well as handle motion with optical flow algorithms on temporal nets.  


# C: IMPLEMENTATION

* The performance of the computer vision machine will depend on its implementation details: architectures, data prep, GPUs, training methods, etc.  Our architecture has different "building bloc" layers (i.e. pooling/convolutional layers) that capture patterns in video as edges, parts and objects.

* What is the "secret sauce" boosting 2 stream architecture?
* What is applied after each convolutional layer?
* How do enable learning of spatiotemporal features at all possible scales?
* Where to fuse 2 nets? 
* How to fuse the 2 nets (at a conv layer) so that channel responses at the same pixel position are put into correspondence?  

# PRETRAINING

# TRAINING 

* ReLU
* Batch Normalization
* Mutli-Task Learning

# TESTING

* Data Augmentation

# MULTI-GPU TRAINING

# OPTICAL FLOW RESCALING

# D: EVALUTATIONS

	# DATA SETS
	# SPATIAL NETS
	# TEMPORAL NETS
	# MULTI-TASK LEARNING

# EXPERIMENTS 	

# CONCLUSIONS

# FUTURE RESEARCH?

* Teaching machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs as real-time computer vision applications face a strict bandwidth-accuracy trade-off
* Underpinning modern tools with a public log of all queries run on video stream data to give guests better idea about how their data is used
* Restructing code and making arrays more ergonomic 
* Determining the metrics that improve downstream performance
* Lowering the costs of switching data between neighborhood shops
* Making up for the data set bias that leads to decreased generalization
* Data Exchange - Letting clients/customers share and sell their data for training computer vision models
* Better understanding how social, economic and legal systems work together to achieve my research goals 

# APPENDIX A:  PROOF-OF-CONCEPT

* Outline area around humans entering/exiting a building with a rectangle and update total number inside building accordingly.

01 Installing Required Packages and Libraries
* Python
* OpenCV https://opencv.org/
* dlib http://dlib.net/a

02 Configuring the Edge Computing Device (Raspberry Pi)

03 Footfall/People Counter (See Attached Code)
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
	
# APPENDIX B HUMAN ACTION CLASSES

* Working List for Neighborhood Shop Applications 
	* Answering Questions
	* Bartending
	* Cleaning Floor
	* Cash Payments
	* Guests Drinking
	* Guests Eating
	* Extinguishing Fire
	* Garbage Collection
	* Hugging
	* Laughing
	* Making Food
	* Making Coffee Beverages
	* Pushing Cart
	* Shaking Hands
	* Sign Language Interpreting
	* Guest Smoking/Vaping
	* Guests Browsing Goods
	* Guests Putting Goods in Basket/Bag
	* Sweeping Floor
	* Stocking
	* Mopping Floor
	* Water Plants
	* Petting Animals
	* Unboxing Goods
	* Sickness/Injury

# APPENDIX C: POLICY MEMORANDUM

* The introduction of modern, legally enforceable computer vision privacy rights will be politically fraught.  Reform must keep up the long, hard slog of countering implicit bias, cementing privacy rights and building the infrastructure to uphold them.  I truly believe computer vision privacy rights should be for all, not just the few. Those building computer vision applications must accept greater responsiblity for its future with a collectively made set of rules with its own checks and balances.

# ACKNOWLEDGEMENTS

* This work was supported by my immediate family, my lovely partner Kristen, my close friends and confidants and the open source community. 

# REFERENCES

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* Deep Learning, An MIT Press Book (2016)
* The Great Good Place by Roy Oldenburg (1989)

* "ImageNet Classification with Deep Convolutional Neural Networks" (20xx)
* "The Kinetics Human Action Video Dataset" (2017)
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "MatConvNet Convolutional Neural Networks for MATLAB" (2016)
* "Spatiotemporal Residual Networks for Video Action Recognition" (2016)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Convolutional Two-Stream Network Fusion for Video Action Recognition" (2016)
* "Return of the Devil in the Details: Delving Deep into Convolutional Nets" (2014)
* "Towards Good Practices for Very Deep Two-Stream Convnets" (2015)

* "Action Recognition with Trajectory-Pooled Deep-Convolutional Descriptors" (2015)
* "A Duality Based Approach for Realtime TV-L1 Optical Flow" (20__)
* "Recurrent Batch Normalization" (2017)
* "Action Recognition with Improved Trajectories" (2013)

