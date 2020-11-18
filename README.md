*** WORKING PAPER ***

*** ATTACHED CODE >> Proof of Concept, Image Classifier ***

## 1 INTRODUCTION

* Corner stores do more than provide us with essential goods. They are where unrelated people relate. They are a place you go for the simple pleasure of good conversation. The corner store represents the social infrastructure key to safety and prosperity in our young Midwestern cities. Tho our corner stores are amidst a once-in-a-generation shift, as technology becomes more baked into everyday life. 
* This research explores ways to extend the idea of what a corner store could be. With the help of many other great minds we develop, deploy and manage computer vision applications that make corner stores more simple and certain. Our goal is to build secure handheld computer vision machines, and supply more industries with implementations, architectures, data sets and mixed-methods teams dedicated to the entire process.

## 1.1 HOW DO WE BUILD COMPUTER VISION MACHINES?

* We do this by building social graphs of the connections between people and goods (i.e. human-object interactions) in corner stores.  Tho many challenges come with this approach.  Corner stores' raw video streams have redundant frames so processing takes time, storage is huge and they are often bottlenecks during training.  So how do we model social graphs across longer video stream timespans accurately, efficiently and with an ability to generalize?  We use Neuro-Ethnographic Reasoning.  Our model builds its social graphs around asking descriptive ("how many? is there?"), explanatory ("what is responsible for?"), predictive ("what will happen?"), counterfacutual ("what if?") and ethnographic research questions. 
* There is still no clear front runner for computer vision machine architectures. Classficiation errors reflect a general weakness of quantitative modeling: overestimation.  Our ultimate goal is to create Neuro-Ethnographic social graphs - in which data from off-the-shelf cameras are collected, thoughtfully processed and fed into corner store applications in real-time.

## 1.2 CORNER STORE APPLICATIONS 

* Corner stores must evolve with shoppers' changing ideas of convenience. Our real-time computer vision machines merge all data silos - video streams, financial records, service notes - into a single platform.  Next machines are trained on thoughfully collected data that enables them to better handle complex corner stores scenarios. Working alongside flesh-and-blood workers the machines allow humans to move beyond their exisiting roles, positions and expectations to a more vibrant dynamic. 
	* WhatYouAlmostBoughtApp >> Detect shoppers' cross product interactions to better understand product positioning strategies and recommend yet more products
	* AutonomousCheckoutApp >> Keep track of human-object interactions to build 'running tabs' for each shopper along with automatic payments options   

## 2 RELATED WORKS

## 3 VERY DEEP MULTI-STREAM NETWORK

* Our computer vision machine consists of an off-the-shelf camera & Nvidia Jetson Xavier NX running a:
	* spatial network that recognizes objects
	* a temporal network that recognizes actions 
	* an optical flow network that captures temporal structure (i.e. objects put in a shopping bag vs. objects removed from shopping bag).  

## 3.1 SYSTEM ARCHITECTURE

* Our architecture handles data pre-processing, model training, data-post procoessing, investigating and fixing performance bottlenecks, etc. We rely on NVIDIA's Jetpack SDK for libraries, APIs, debugging kits and optimization.  We create a deep architecture to encode representations into the very deep multi-stream network to better recognize human-object interactions in raw unseen corner store video streams.

## 3.2 NETWORK PRETRAINING 

* We use a variant of ImageNet model to pretrain our multi-stream network (i.e. spatial, temporal, optical flow). We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across 22k categories. Pretraining allows us to avoid representational bottlenecks, boost activations per tile, make for easier dimensional reduction and better balance the width and depth of the network.

## 3.3 DATA AUGMENTATION

## 3.4 NETWORK TRAINING

* We train our computer vision machines on our "Behaviorgram" dataset (see 5.1) which enables us to experiment with a diversity of research approaches, and fine-tune our architectures to navigate uncertainity better, faster and with less computational energy.

## 3.5 NETWORK ARCHITECTURE

## 3.6 IMPLEMENTATION

## 4 EXPERIMENTS

* In this section we explore the generalizability of networks trained on three different datasets.
* Because training datasets take up many GBs in memory, a 500 GB disk is added and mounted on the virtual machine for dataset storage. The GPU chosen is a NVIDIA Tesla P100 for inferences in the cloud and a NVIDIA Jetson Xavier XN for performing inferences on the edge. 

## 4.1 "BEHAVIORGRAM" DATASET

* Bias is inevitable when training computer vision models for human action detections in video streams. To combat this we apply ethnography to build datasets that better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what humans feel is important. Our reality is political, but the dominant groups claim as the norm when training computer vision machines need not be the dominant view.  Our data prep hones years worth of local corner store knowledge to build a human-object interaction social graphs, which are publicly available. Our approach asks descriptive ("how many? is there?"), explanatory ("what is responsible for?"), predictive ("what will happen?"), counterfacutual ("what if?") and ethnographic research questions. This approach takes qualitative and analog methods, and turns it into something that addresses shortcomings in ourtraining datasets.  

* So what is ethnography? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world (i.e. local knowledge, preferences, values, beliefs). Ethnographic labels include the knowledge embedded in the heads of corner store staff and its regulars.  Labels include: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots and unstated goals.  Guided by ethnography, we hand label human-object interactions in a set of video streams, in order for the computer vision models to be able to learn what actions look like from a variety of different angles, biases, etc.  Once the models have digested these video streams, the algorithms are let loose on raw unseen corner store video streams.

* STEP 1 DataCollection - Descriptive, Explanatory, Predictive, Counterfactual and Ethnographic field notes
* STEP 2 TidyDataSet - In-house autonencoder makes use of collected data that are semantically similar to label human-object interactions in video streams
* STEP 3 ReproducibilityRecipe - Set up calculations in a way that promotes common data standards and portability across corner stores for better flow of data

* "Behaviorgram-v1" Dataset
	* 6 Actions each, across 20 Groups
	* 40 Clips per Group 
	* 4800 Clips @ 3-12 seconds each
	* 30 fps 
	* 640 x 480
	* Audio: YES

## 4.2 UCF-101 DATASET

* 13320 videos across 101 action classes

## 4.3 HMDB-51 DATASET

* 6766 videos across 51 action classes

## 5 ENSURING DATA PRIVACY

* Dr Ben Goldacre of Oxford and his colleagues May 2020 approach to studying the medical records of 17m people in Britain inspired our privacy practices.  Their team developed software that let them run analysis without copying or moving data out of that data center. Instead they poked data thru a secure connection, with a log of all queries run on the medical records to create an audit trail. Their open source methods perserved confidentiality while freeing high value information for analysis. It also gave the public a better idea about how their data is used. We designed and built our computer vision machine and its applications with this approach to privacy in mind.

## 6 DISCUSSION

## 7 SANDBOX

* Teaching computer vision applications to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs 
* Rewriting code and making arrays more ergonomic (hashing trick?) 
* Determining the metrics that improve downstream performance
* Lowering the costs of switching data between corner stores
* Data Exchange? helping clients/customers share and sell their data for training computer vision models
* Better understanding how social, economic and legal systems work together to achieve research goals 

## APPENDIX A: POLICY MEMORANDUM

* The introduction of modern, legally enforceable computer vision privacy rights will be politically fraught.  Reform must keep up the long, hard slog of countering implicit bias, cementing privacy rights and building the infrastructure to uphold them. Those building computer vision applications must accept greater responsiblity for its future. We must be part of setting the agenda, attitute, culture and laws around computer vision privacy rights.

## ACKNOWLEDGEMENTS

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
* "Recurrent Batch Normalization" (2017)
* "FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks" (2016)
* 
* "CLEVRER: Collision Events for Video Representation and Reasoning" (2020)
* "Mimetics: Towards Understanding Human Actions Out of Context" (2020)
* "Deep Temporal Linear Encoding Networks" (2016)
