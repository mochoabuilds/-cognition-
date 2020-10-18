*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT: Appendix A ***

# WHAT IS IT?

* This research helps computer vision machines better understand the difference between 'just seeing' and actually observing.  The hope is to see what is invisible to others. This research extends the idea of what a neighborhood shop could be. With the help of some great minds we develop open source tools make shopping more simple and certain.

# WHY? (SOCIAL REASONS)

* Neighborhood shops do more than provide us with essential goods. They are where unrelated people relate. They are a place you can go for the simple pleasure of good conversation. The neighborhood shop represents the social infrastructure that is key to safety and prosperity in our young midwestern cities. However, our neighborhood shops are transforming. They're now living laboratories for new communal safety habits.  Our goal is to make neighborhood shops nore robust and resilient, and rework the pipes channeling money and data to make them more simple and certain.

# WHY? (OTHER REASONS)

* We want to drive an industry of secure computer vision machines, and supply the industry with architectures, datasets, implementations and a mixed-methods team dedicated to the process.

# RELATED WORKS

# HOW WE DID IT? (TLDR)

* The computer vision machine is a low light camera & Nvidia Jetson TX2 running a optical flow network, spatial network, temporal network and support vector machine (SVM) to detect human-object ineractions in neighborhood shops.

# COMPUTER VISION APPS FOR NEIGHBORHOOD SHOPS

* InventoryApp >> Smartphone notifications provide immediate, actionable data on human interactions with shop inventory
* WhatYouDidntBuyApp >> Smartphone interface detects guests' cross product interactions to better understand product positioning strategies, etc.
* CheckoutApp >> Smartphone app keeps track of human-object interactions and builds 'running tabs' for each shopper along with an automatic payments option to make shopping more simple and certain

# OVERALL ARCHITECTURE

* Camera > Action Recognition Model & Flash Storage > Modem > Cloud > Smartphone Apps

# "TwO STREAM" CONFIGURATION

* This section provides the technical contributions for running a spatial network, optical flow network, temporal stream and SVM to identify human-object interactions in neighborhood shops as action class probabilities. We then use a deep architecture to encode deep learned representations into the net to better recognize human-object interactions classes in raw unseen neighborhood shop video frames.

# PRETRAINING

* We used ImageNet to pretrain two streams (spatial & temporal). We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across 22k categories. We pretrain to avoid representational bottlenecks, boost activations per tile, make for easier dimensional reduction and better balance the width and depth of the network.
* The performance of the computer vision machine running neighborhood shop applications will depend on its implementation details (i.e. architectures, data sets, training methods, activation functions, etc.) 

# ARCHITECTURE FOR CLASSIFICATION

* Our architecture has different "building bloc" layers (i.e. pooling/convolutional layers) that capture patterns in video as edges, parts and objects to help the machine better generalize to longer sequences than those seen during training.

# EXPERIMENTAL EVALUATIONS A,B,C

* In this section we explore the generalizability of networks trained on different datasets.

# A: NEIGHBORHOOD SHOP DATASET

* Bias is inevitable when training computer vision models for human-item recognition. To combat this we blend qualitative and quantitative methods to better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what humans feel is important. Our reality is political, but the dominant groups claim as the norm when building computer vision applications need not be the dominant view.  Our data prep hones years worth of local knowledge in neighborhood shops to build a low-light human-object neighborhood shop dataset, which is publically avaliable.

* STEP 1 RawData - What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world (i.e. local knowledge, preferences, values, beliefs). Ethnographic labels include the knowledge embedded in the heads of neighborhood shop staff and its regulars.  Labels include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, etc. 
* STEP 2 TidyDataSet - In-house autonencoder makes use of ethnographic labels that are semantically similar to label human-object interactions
* STEP 3 ReproducibilityRecipe - Set up calculations in a way that promotes common data standards and portability across neighborhood shops for better flow of data

* NeighborhoodShop Dataset
	* 6 Actions w/ 20 Groups & 40 Clips per Group 
	* 4800 Clips at 3-4 seconds each 
	* 30 fps 
	* 640 x 480
	* Audio: YES

# B: UCF-101 DATASET

# C: HMDB-51 DATASET

# DISCUSSION

# FUTURE RESEARCH

* Teaching machines to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs as real-time computer vision applications face a strict bandwidth-accuracy trade-off
* Underpinning modern tools with a public log of all queries run on video stream data to give guests better idea about how their data is used
* Restructing code and making arrays more ergonomic 
* Determining the metrics that improve downstream performance
* Shallow architecture?  Compressing networks with hashing trick?
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

# APPENDIX B: POLICY MEMORANDUM

* The introduction of modern, legally enforceable computer vision privacy rights will be politically fraught.  Reform must keep up the long, hard slog of countering implicit bias, cementing privacy rights and building the infrastructure to uphold them.  I truly believe computer vision privacy rights should be for all, not just the few. Those building computer vision applications must accept greater responsiblity for its future. They must be part of setting the agenda, attitute, culture and laws around computer vision privacy rights.

# ACKNOWLEDGEMENTS

* This work was supported by my immediate family, my lovely partner K, my close friends and confidants and the open source community. 

# REFERENCES

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* Deep Learning, An MIT Press Book (2016)
* The Great Good Place by Roy Oldenburg (1989)
*
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Rethinking the Inception Architecture for Computer Vision" (2015)
* "Going Deeper with Convolutions" (2014)
* "Temporal Segment Networks: Towards Good Practices for Deep Action Recognition" (2016)
*
"Action Recognition with Improved Trajectories" (2013)
* "A Duality Based Approach for Realtime TV-L1 Optical Flow" 
* "Recurrent Batch Normalization" (2017)

By Michael Valentino Ochoa
