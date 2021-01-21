*** "An Actionable Credit System for Cashierless Checkout"

*** Attached Code:  Packaged Goods Classifier (Proof of Concept) 

## 1 CIRCUMSTANCES OF CONCEPTION

* During Spring 2020, when visiting my neighborhood corner store in Chicago my plan was to scoop some essentials.  Waiting in a line that snaked up and down the aisles I maintained my physical distance on account of COVID-19 restrictions.  Yet the line stretched too far and  new shopper entered, so I was left momentairly stuck between some loud talkers not wearing masks.  After a few anxious minutes I exited, immediately thinking there must be a better way for regular customers to do checkout at the corner store. 

## 1 INTRODUCTION

* Advances in machine learning have given corner stores far shinier toolkits.  Tools have gotten smaller, parallelised and now run along with smartphones, progress has become very fast. As computer vision improves, this could spark major improvements in how corner stores run their business.  This research function as a mediator for the emerging corner store checkout experience. 

## 1.2  PURPOSE / PROBLEM SOLVED

* Hyperlocal by nature, corner stores are inherently loyal to their surrounding neighborhood. Many souls been known to benefit from handshake deals that let them grab goods on credit. This socio-economic infrastructure can't be underestimated. Their prescence can't be underestimated.  

* To transform the corner store toolkit, and not just its IT department, we take mature open-source software and embed it in services everyone can trust. Our system assembles all the knowledge scattered throughout the corner store and translates it in ways that the system can use to create new tools.

* Our tools revolve around the idea that: people don't want to make payments, they want to do what a payment facilitates.  Some regulars want the option to grab goods on credit and simply skip the line entirely.  They want their corner store to be part pantry / part place to say hello.  Such spaces are key to safety and prosperity in your young midwestern cities.   We offer these regulars an intelligent AI solution that makes for a simplier, clearer and more hospitable checkout experience.

* Walk in > Tap a tile > Shop > Walk out

* What unique about our approach is that it accesses AI programs both remotely and locally rather than installing them on big old actual computers.  Instead computations are done on hand sized computing devices equipped with their own cameras - tools/apps are highly automated, readily avaliable and easy-to-use.  Prototypes include:
	* Autonomous Checkout >> System watches guests browse shelves, keeps a running tab of items taken from shelves and prompts guests with SMS payment upon exit
	* What You "AlmostBought" App >> Detect guests cross product interactions to better understand product positioning strategies 
	* Data Exchange >> Guests share and sell their data for training machine learning models

## 1.3 HOW WILL WE DO IT?

* To address our biggest challenge, the impracticality of approaching every machine learning problem with brute computing power, we looked for shortcuts. Rather than having our computer vision system see corner store scenarios thru step by step thinking, ours sees scenarios with its own "intuition".  It learns that from translated rules of thumb about how people shop and leave happy that humans also lean on, but struggle to articulate. Our in-house autoencoder does the translating of these ethnographic field data on how hopstiable shopping experience happens with a human, and translating that into rules of thumb that make real world scenarios more understandable to our tools/apps.  This is not our original system, but our current approach gives us more room to grow and boost our technology's accuracy. We have tried dozens of different ways to construct an autonomous checkout system before designing this one from scratch.  
	
## 2 RELATED WORKS

## 3 METHODS


## 3.1 SYSTEM OVERVIEW

* Our system consists of an off-the-shelf camera and Jetson Xavier NX embedded computing board that runs our code using NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization. The goal is to create a 'digital twin' of a corner store that integrates real-time data from off-the-shelf cameras to display the state of the shop at any given time, and extend that understanding towards autonomous checkout.  Using off-the-shelf cameras, embedded computing boards and AI models our system better understands guest behaviors and preferences at any given time. The computing board is optimized using NVIDIA's Metropolis framework to performs real-time computations of AI algorithms on the edge.  This system tests and measures the success of autonomous checkout accuracy rates and extends these valuable insights to corner stores across the system.

## 3.2 DOWNLOAD OPEN SOURCE MODELS (PRETRAINING)

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across thousands of  categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and helps us better balance the width and depth of the network.

## 3.3 LABEL TRAINING DATASETS

* Bias is inevitable when training machine learning models for human action-object detections in video streams. To counter  corner stores are the center of our analysis, to better debase the dominant groups claim as the norm for theories about how guests shop / leavier happier. Our reality is political, but the Ai developer perspective as the norm when training AI applications need not be. We believe this approach helps the models better "see" the sensitive interpretations of what humans feel is important.  

* Our IN-HOUSE AUTOENCODER compresses human rules of thumb/labels/vectors from staff and loyal regulars into short binary codes that AI models use to "see" corner stores with their own hyperlocal "intuition".  This "intuition" helps AI models generalize to longer sequences than those seen during training.  It also helps us combine several store datasets to learn neighborhood level human-object representations, and easily add rich training data on the fly.


* STEP 1 >> DataCollection - Hand labeling of human rules of thumb into video streams
* STEP 2 >> TidyDataSet - In-house "ethnographic autonencoder" notices human-object interactions that are semantically similar to hand labeled human rules of thumb from previous video streams
* STEP 3 >> ReproducibilityRecipe - Set up classification calculations in a way that promotes common data standards and portability to decrease overfitting models.

* Our IN HOUSE LABELED DATASET currently consists of 100 human action classes with 100 clips per class each lasting 10 seconds.

## 3.4 CONFIGURE PLATFORMS/FILES

## 3.5 CUSTOM INTEGRATIONS 

## 3.6 MODEL ARCHITECTURE 

* Baed on the human visual cortex, our model contains two pathways the ventral (shape and color of objects) and the dorsal (caused by motion of objects).  This approach helps us better represent motion using the optical flow displacement field.  A two stream approach also helps the model better understand how repetitive actions such as "sweeping" require an understanding of different spatiotemporal cues at different scales, a tricky work of human fine-tuning.

## 4 EXPERIMENTAL EVALUATION 

* In this section we explore the accuracy/generalizability of models on different benchmark data sets.

## 4.1 UCF-101 DATASET

* 13320 videos across 101 action classes

## 4.2 HMDB-51 DATASET

* 6766 videos across 51 action classes

## 5 DISCUSSION

## APPENDIX: BI-DIRECTIONAL COMMUNICATIONS

* In this section we describe how we send and recieve event triggered messages between cloud and device / request system logs / conduct model updates.

## SANDBOX

* Teaching computer vision applications to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs 
* Rewriting code and making arrays more ergonomic
* Determining the metrics that improve downstream performance
* Lowering the costs of switching data across different corner stores
* Better understanding how social, economic and legal systems work together to achieve research goals 

## ACKNOWLEDGEMENTS

* This work was supported by my lovely partner K, my immediate family, my close friends and confidants and the open source community. 

## REFERENCES

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* Deep Learning, An MIT Press Book (2016)
* The Great Good Place by Roy Oldenburg (1989)
* Interaction of Color by Josef Albers (1963)
*
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Rethinking the Inception Architecture for Computer Vision" (2015)
* "Going Deeper with Convolutions" (2014)
* "Temporal Segment Networks: Towards Good Practices for Deep Action Recognition" (2016)
* "Deep Residual Learning for Image Recognition" (2015)
* "FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks" (2016)
* "A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow and Scene Flow Estimation" (2016)


