*** WORKING PAPER ***

*** ATTACHED CODE:  Packaged Goods Classifier - Proof of Concept ***

## 1 SUMMARY

* The shift to mobile payments requires a service that makes checkout more simple and certain. Our research deploys AI technology to spark major improvements in how corner stores/small grocers run their businesses.  We enable them to conduct autonomous checkout for goods via SMS.  By taking the idea of waiting in line out of the equation we make checkout more simple and certain. The shift to mobile payments, plus our magic will create a network effect among partnering stores, making our service the preferred way to pay in person.

## 1.1 INTRODUCTION

* Corner stores - part pantry, part place to hug the block. To be honest, their prescence can't be underestimated.  Hyperlocal by nature, corner stores are inherently loyal to its surrounding population. Many have been known to benefit from understandings that let them grab goods on credit. We believe this socio-economic infrastructure is key to safety and prosperity in Midwestern cities. 

## 1.2 WHY FOCUS ON CORNER STORES? 

* To win in the corner store market today, you gotta build loyal regulars.  Its hyperlocal nature means word of a better experience will go around quickly.

* Our service accesses AI programs remotely rather than installing them on actual computers -- so applications are highly automated, easy-to-use and readily avaliable. 
	* Autonomous Checkout App >> Watch shoppers browse shelves, keep a running tab of items taken from shelves and charge shoppers upon exit
	* WhatYouAlmostBought App >> Detect shoppers' cross product interactions to better understand product positioning strategies 
	* Data Exchange >> Shoppers share and sell their data for training computer vision models

## 1.3 HOW WE DO IT?

* To transform the corner store, not just its IT department, our approach takes mature open-source software and embeds it in services everyone can trust. A culture of test-driven development, human-centered design and edge-cloud operations drive our theory and methods. Our mixed methods approach blends rich ethnographic data from humans with powerful AI models to create a portfolio of services that are highly automated and easy-to-use. We strive to help stores run applications that make services more simple and certain.
	
## 2 RELATED WORKS

## 3 THEORY + METHODS

* To address our biggest challenge - the impracticality of approaching every AI problem with brute computing power - we looked for shortcuts. Rather than having our AI models see corner store scenarios as step by step thinking, models see these scenarios with their own "intuition" learned from many translated rules of thumb that humans also use, but struggle to articulate. 
* AI is a box of many different tools, and this is not our original system, but our approach gives us more room to grow and boost the technology's accuracy further. We have tried dozens of different ways to construct a AI/computer vision system before designing this one from scratch.  It is both functional and manufacturable.  

## 3.1 SYSTEM OVERVIEW

* Our system consists of an off-the-shelf camera and Jetson Xavier NX embedded computing board running our magic/code/data via NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization.

## 3.2 UPLOADING/PRETRAINING NETWORK

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across 22k categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and better balance the width and depth of the network.

## 3.3 COLLECTING TRAINING DATA ("ETHNOGRAPHIC AUTOENCODER")

* Bias is inevitable when training computer vision models for human action-object detections in video streams. To combat this we build datasets that better debase the dominant groups claim as the norm. Our reality is political, but the dominant groups claim as the norm when training computer vision machines need not be. This helps our AI models better "see" the sensitive interpretations of what humans feel is important. Our "ethographic autoencoder" translates human rules of thumb from staff and loyal regulars into a lanugage machines use to "see" corner stores with their own hyperlocal "intuition". 

* STEP 1 >> DataCollection - Video Streams & Hand Labeling 
* STEP 2 >> TidyDataSet - In-house hand-labeling/autonencoder makes use of collected data that are semantically similar to label human-object interactions in video streams
* STEP 3 >> ReproducibilityRecipe - Set up classification calculations in a way that promotes common data standards and portability across multiple corner stores for better flow of data

## 3.4 ADDING NETWORK LAYERS

## 3.5 TRAINING THE MODEL

## 3.6 TESTING THE MODEL

## 4 EXPERIMENTS

* In this section we explore the accuracy/generalizability of AI models on different benchmark data sets.

## 4.1 UCF-101 DATASET

* 13320 videos across 101 action classes

## 4.2 HMDB-51 DATASET

* 6766 videos across 51 action classes

## 4.3  CORNERSTORE-112 DATASET

## 5 DISCUSSION

## 6 SANDBOX

* Teaching computer vision applications to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs 
* Rewriting code and making arrays more ergonomic
* Determining the metrics that improve downstream performance
* Lowering the costs of switching data across different corner stores
* Better understanding how social, economic and legal systems work together to achieve research goals 

## APPENDIX A: POLICY MEMORANDUM

* The introduction of modern, legally enforceable computer vision privacy rights will be politically fraught.  Reform must keep up the long, hard slog of countering implicit bias, cementing privacy rights and building the infrastructure to uphold them. Those building computer vision applications must accept greater responsiblity for its future. We must be part of setting the agenda, attitute, culture and laws around computer vision privacy rights.

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


