*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT: Plz See Appendix A) ***

# WHAT IS IT?

* This research helps computer vision machines better understand the difference between 'just seeing' and actually observing.  The hope is to see what is invisible to others by better taking into account the lighting, textures and reflectivity of different objects, human actions and events in neighborhood shops.  This research extends the idea of what modern tools for neighborhood shop could be. With the help of some great minds we develop open source tools to analyze neighborhood shop video streams with high classification accuracy and reasonable computational costs. 

# WHY? (SOCIAL REASONS)

* Neighborhood shops do more than provide us with essential goods. They are where unrelated people relate. They are a place you can go for the simple pleasure of good conversation. The neighborhood shop represents the social infrastructure that is key to safety and prosperity in our young midwestern cities. However, our neighborhood shops are transforming.  They're now living laboratories for new communal safety habits.  Our goal is to rework the pipes channeling money and data in neighborhood shops to make them more simple and certain.

# WHY? (TECH REASONS)

* We want to drive an industry of secure computer vision machines, and supply the industry with architectures, datasets, implementations and a mixed-methods team dedicated to the process. "Sometimes long-term simplicity is achieved only through bursts of complexity that rework current systems." 

# RELATED WORKS

# HOW WE DID IT? (TLDR)

* We used ImageNet to pretrain two streams (spatial & temporal).  We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across 22k categories. Next we gathered local knowledge, the kind embedded in the heads of neighborhood staff and its regulars, and used it to label human actions that are semantically similar. I then trained an autoencoder to compress these labels into short binary codes... 
* To be continued

# WHY COMPUTER VISION APPLICATION FOR NEIGHBORHOOD SHOPS?

* Shops need immediate, actionable data to improve customer experiences. We solve this problem by integrating real time data from video cameras across the shop to display the state of the shop @ any given time, and build end-to-end computer vision applications and tools that look into the future as the basis for simulations in events.

* Inventory Assistant >> An interface that recognizes human interactions with inventory to generate real-time reports
* "What You Didn't Buy" Assistant >> An interface for understanding guests' cross product interactions to better understand market segmentation and product positioning strategies
* Autonomous Shopping >> A cashier mgmt system that recognizes human actions to build guest shopping carts in real-time; generate AR/AP, cash flow statements and general ledgers.  "People don't want to make payments, they want to do what a payment facilitates."


# COUNTERING BIAS

* Bias is inevitable when training computer vision models for human action recognition. To combat this we blend qualitative and quantitative methods to better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what humans feel is important. Our reality is political, but the dominant groups claim as the norm when building computer vision applications need not be the dominant view.  Our data prep hones years worth of local knolwedge in neighborhood shops to build a computer vision machine.

* STEP 1 RawData >> What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world (i.e. local knowledge, preferences, values, beliefs). Field notes include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, etc. 
* STEP 2 TidyDataSet >> In-house Autonencoder that makes use of ethnographic labels to better retrieve video that is semantically similar
* STEP 3 ReproducibilityRecipe >> Set up calculations in a way that is easy for reproducibility 

# PRETRAINING

* We pretrain our two streams with Inception-V3 to avoid representational bottlenecks, boost activations per tile, dimensional reduction before spreading to larger convolutions and to balance the width and depth of the network. This methods helps the computer vision machine better analyze vague hints and 'hallucinate' the finer details to detect small neighborhood shop objects.
	
# TWO STREAM CONFIGURATION

* This section provides the technical contributions for fusing two streams (spatial & temporal). The spatial net detects high motion regions and captures static cues such as the shape and color of objects related to actions.  Whereas the temporal net describes what is happening in high motion regions. Next, we use a deep architecture to encode deep learned representations into the spatial net to recognize human action classes in raw unseen neighborhood shop video with high classficiation accuracy.
* Fig 1.

# IMPLEMENTATION

* The performance of the computer vision machine will depend on its implementation details: architectures, data sets, training methods, etc. 
* Activation Functions: ReLU, Batch Normalization
* Data Augmentation: 
* Multi-Task Learning:

# ARCHITECTURE

* Our architecture has different "building bloc" layers (i.e. pooling/convolutional layers) that capture patterns in video as edges, parts and objects to help the machine generalize to longer sequences than those seen during training.
* Fig 2.

# EXPERIMENTAL EVALUATIONS	

# CONCLUSIONS

# FUTURE RESEARCH

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

* This work was supported by my immediate family, my lovely partner K, my close friends and confidants and the open source community. 

# REFERENCES

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* Deep Learning, An MIT Press Book (2016)
* The Great Good Place by Roy Oldenburg (1989)

* "ImageNet Classification with Deep Convolutional Neural Networks" (20xx)
* "The Kinetics Human Action Video Dataset" (2017)
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "MatConvNet Convolutional Neural Networks for MATLAB" (2016)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Towards Good Practices for Very Deep Two-Stream Convnets" (2015)
* "Action Recognition with Trajectory-Pooled Deep-Convolutional Descriptors" (2015)
* "A Duality Based Approach for Realtime TV-L1 Optical Flow" (20__)
* "Recurrent Batch Normalization" (2017)
* "Action Recognition with Improved Trajectories" (2013)

