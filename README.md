*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT: Plz See Appendix A) ***

# WHAT IS IT?

* My research extends the idea of what a neighborhood shop could be.  With the help of some great minds I develop open source tool to analyze neighborhood shop video streams and build computer vision applications that have high classification accuracy and reasonable computational costs.  My hope is to showcace more fluid ways to perform day-to-day operations using applications of the mathematical & social sciences. 

# WHY? (SOCIAL REASONS)

* Neighborhood shops do more than provide us with essential goods. They are where unrelated people relate. They are a place you can go for the simple pleasure of good conversation. However, our neighborhood shops are also transforming.  They're now living laboratories for new communal safety habits.  My goal is to use everyday theorizing to provide neighborhood shops with fluid tools for our new era.

# WHY? (TECH REASONS)

* Computer vision methods have shown termendous promise for scene analysis when trained on large datasets.  However current datasets for neighborhood shop scene analysis are small and limited to mundane environments that don't capture the complexity of the neighborhood shop. 

# RELATED WORKS

# HOW? (TLDR)

* A whole new machine was created to build these neighborhood shop computer vision applications. First, I gathered local knowledge, the sort embedded in the heads of neighborhood staff and its customers, and used it to label video that is semantically similar. I then trained an autoencoder to compress these local knowledge labels into short binary codes. These labels help computer vision models learn how action cues change over time to better understand the temporal evolution of human actions in neighborhood shops scenes.

# NEIGHBORHOOD SHOP APPLICATIONS

* "Sometimes long-term simplicity is achieved only through bursts of complexity that rework current systems." 

	* 01_Inventory Assistant >> An interface that recognizes human actions with inventory and generates reports
	* 02_"What You Didn't Buy" Assistant >> An interface for understanding guests' cross product interactions to better understand market segmentation and product positioning strategies
	* 03_Autonomous Checkout >> A cashier mgmt system that recognizes human actions to build guest shopping carts in real-time; generate AR/AP, cash flow statements and general ledgers
	
# A. METHODS (DATA PREP)

* Bias is inevitable when training computer vision models for human action recognition. To combat this we blend qualitative and quantitative methods to better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what humans feel is important. Our reality is political, but the dominant groups claim as the norm when building computer vision applications need not be the dominant view.  Our data prep hones years worth of local knolwedge in neighborhood shops to build a computer vision machine.

* STEP 1 RawData >> What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world (i.e. local knowledge, preferences, values, beliefs). Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, etc. 
* STEP 2 TidyDataSet >> In-house Autonencoder that makes use of ethnographic labels to better retrieve video that is semantically similar
* STEP 3 ReproducibilityRecipe >> Set up calculations in a way that is easy for reproducibility 
	
# B. ARCHITECTURE PROPOSED FOR BOTH STREAMS 

* This section provides the technical contributions for fusing two convolutional nets (spatial & temporal). The spatial net detects high motion regions and captures static cues such as the shape and color of objects related to actions.  Whereas the temporal net describes what is happening in high motion regions. Next, we use a deep architecture to encode deep learned representations into the spatial net to recognize human action classes in raw unseen neighborhood shop video with high classficiation accuracy.

* Challenges in human action recognition in video: low video resolution (224 x 224), learning complex motion patterns and styles, background clutter, high dimensionality of video data and small datasets for training very deep models.   


# C: IMPLEMENTATION

* The performance of the computer vision machine will depend on its implementation details: architectures, data prep, GPUs, training methods, etc.  Our architecture has different "building bloc" layers (i.e. pooling/convolutional layers) that capture patterns in video as edges, parts and objects to help the machine generalize to longer sequences than those seen during training.

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

