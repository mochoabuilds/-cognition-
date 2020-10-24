*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT: Appendix A ***

## 1 INTRODUCTION

* Neighborhood shops do more than provide us with essential goods. They are where unrelated people relate. They are a place one can go for the simple pleasure of good conversation. The neighborhood shop represents the social infrastructure key to safety and prosperity in our young Midwestern cities. Tho our neighborhood shops are transforming. They've become living laboratories for new communal safety habits. This research builds computer vision applications that extends the idea of what a neighborhood shop could be. With the help of some great minds we develop software tools that make shopping more simple and certain.

* Our goal is drive an industry of secure computer vision machines, and supply industry with implementations, architectures, datasets, implementations, applications and a mixed-methods team dedicated to the process.

## 1.1 COMPUTER VISION APPS 

* Our applications merge all the data silos that a neighborhood shop collects - video streams, financial records, service notes - into a single platform.  Merged data is then presented as an elegant easy to use smartphone apps.
* InventoryApp >> Smartphone interface providing immediate actionable data about human-object interactions with shop inventory
* WhatYouAlmostBoughtApp >> Smartphone interface detecting guests cross product interactions to better understand product positioning strategies, etc.
* CheckoutApp >> Smartphone interface keeping track of human-object interactions to build 'running tabs' for each shopper along with automatic payments options that make shopping more simple and certain.  

## 2 RELATED WORKS

## 3 HUMAN ACTION DETECTION IN VIDEO STREAMS

* In this section, we give detailed descriptions of our two-stream network for action recognition in video streams. Our prototype consists of a low light camera & Nvidia Jetson TX2 running an optical flow network, spatial network, temporal network and support vector machine (SVM) that detects human-object interactions in neighborhood shops.

## 3.1 SYSTEM ARCHITECTURE, ETC.

Camera > Action Recognition Model & Flash Storage > Modem > Cloud > Smartphone Apps

* We write pipelines for cutting edge computer vision machines  Our pipelines handle data pre-processing, model training, data-post procoessing, investigating and fixing performance bottlenecks, etc.  We run these pipes on edge devices for the sake of privacy and energy use.  More flow diagrams, documentation, testing plans/tools and ongoing support of the machine to come!

## 3.2 TWO STREAM NETWORK (CONFIGURATION)

* This section provides the technical contributions for running a spatial network, optical flow network, temporal stream and SVM that identify human-object interactions as action class probabilities. We use a deep architecture to encode deep learned representations into the networks to better recognize human-object interactions in raw unseen neigborhood shop video streams.

## 3.3 PRETRAINING

* We used ImageNet to pretrain two network streams (spatial & temporal). We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across 22k categories. We pretrain to avoid representational bottlenecks, boost activations per tile, make for easier dimensional reduction and better balance the width and depth of the network.

## 3.4 NETWORK TRAINING

## 3.5 TWO STREAM ARCHITECTURE (CONTINUED)

## 4 ENSURING PRIVACY

* Dr Ben Goldacre of Oxford and his colleagues May 2020 approach to studying the medical records of 17m people in Britain inspired our privacy practices.  Their team developed software that let them run analysis without copying or moving data out of that data center. Instead they poked data thru a secure connection, with a log of all queries run on the medical records to create an audit trail. Their open source methods perserved confidentiality while freeing high value information for analysis. It also gave the public a better idea about how their data is used. We designed and built our computer vision applications with this approach to privacy in mind.

## 5 EXPERIMENTS

* In this section we explore the generalizability of networks trained on different datasets.

## 5.1 NEIGHBORHOOD SHOP DATASET

* Bias is inevitable when training computer vision models for human action detections in video streams. To combat this we apply mixed methods techniques to building datasets to better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what humans feel is important. Our reality is political, but the dominant groups claim as the norm when training computer vision applications need not be the dominant view.  Our data prep hones years worth of local knowledge in neighborhood shops to build a human-object specific neighborhood shop dataset, which is publicly available. Our approach takes ethnography, which many see as qualitative and analog, and turn it into something that trains digital machines.

* STEP 1 RawData - What is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world (i.e. local knowledge, preferences, values, beliefs). Ethnographic labels include the knowledge embedded in the heads of neighborhood shop staff and its regulars.  Labels include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots, unstated goals, etc. 
* STEP 2 TidyDataSet - Our in-house autonencoder makes use of ethnographic labels that are semantically similar to label human-object interactions
* STEP 3 ReproducibilityRecipe - Set up calculations in a way that promotes common data standards and portability across neighborhood shops for better flow of data

* NeighborhoodShop-v1 Dataset
	* Each action, groups and clips tagged with ethnographic field notes
	* 6 Actions with 20 Groups
	* 40 Clips per Group 
	* 4800 Clips at 3-12 seconds each
	* 30 fps 
	* 640 x 480
	* Audio: YES

## 5.2 UCF-101 DATASET

* 13320 videos across 101 action classes

## 5.3 HMDB-51 DATASET

* 6766 videos across 51 action classes

## 6 DISCUSSION

## 7 FUTURE RESEARCH

* Teaching computer vision applications to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs 
* Rewriting code and making arrays more ergonomic 
* Determining the metrics that improve downstream performance
* Compressing networks with hashing trick?
* Lowering the costs of switching data between neighborhood shops
* Making up for the data set bias that leads to decreased generalization
* Data Exchange? helping clients/customers share and sell their data for training computer vision models
* Better understanding how social, economic and legal systems work together to achieve research goals 

## APPENDIX A: PROOF-OF-CONCEPT

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

## APPENDIX B: POLICY MEMORANDUM

* The introduction of modern, legally enforceable computer vision privacy rights will be politically fraught.  Reform must keep up the long, hard slog of countering implicit bias, cementing privacy rights and building the infrastructure to uphold them. Those building computer vision applications must accept greater responsiblity for its future. They must be part of setting the agenda, attitute, culture and laws around computer vision privacy rights.

## ACKNOWLEDGEMENT

* This work was supported by my immediate family, my lovely partner K, my close friends and confidants and the open source community. 

## REFERENCES

* Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
* Deep Learning, An MIT Press Book (2016)
* The Great Good Place by Roy Oldenburg (1989)
*
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "Rethinking the Inception Architecture for Computer Vision" (2015)
* "Going Deeper with Convolutions" (2014)
* "Temporal Segment Networks: Towards Good Practices for Deep Action Recognition" (2016)
* "Deep Residual Learning for Image Recognition" (2015)
* "Batch Normalization: Accelerating Deep Network Training by Reducing Covariate Shift" (2015)
*
* "Action Recognition with Improved Trajectories" (2013)
* "A Duality Based Approach for Realtime TV-L1 Optical Flow" (2007)

