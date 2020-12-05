*** WORKING PAPER ***

*** ATTACHED CODE:  Packaged Goods Classifier - Proof of Concept ***

## 1 INTRODUCTION

* Corner stores do more than provide us with essential goods. They are where unrelated people relate. They are somewhere you go for the simple pleasure of good conversation. The corner store's social infrastructure is key to safety and prosperity in our young Midwestern cities. Tho they are in the throes of a once-in-a-generation shift as mobile/cloud technology becomes more baked into everyday life. To help corner stores, with the help of many other great minds, we develop and deploy computer vision applications that make stores more simple and certain. 

## 1.1 HOW WE DO THIS?

* We believe there is still no clear front runner in computer vision architectures. Classification errors reflect a general weakness of quantitative methods: overestimation. To counter this implicit bias we build rich social graphs of the real-time connections between people and goods in stores.  Our data collection revolves around de-basing the dominant group's claims as the norm for life in corner stores.  Our in-house data sets are working assumptions used to guide "edge cases" computer vision models will inevitably face.  The model's formal theory of the world relates to the corner store, but with a micro and macro understanding of society. Common Q/A collected to encode/decode the world include:
	* "how many?" "is there?"  (descriptive questions)
	* "what is responsible for...?" (explanatory questions)
	* "what will happen?" (predictive questions)
	* "what if?" (counterfactual questions)
	* "members meaning" (rich qualitative questions)
	*  temperature, sound levels, smells (sensory impressions)
	
## 1.2 WHY? 

* Our methods allow us to make sense of patterns and take effective action.  Our theory to building these applications is based on Functionalism (Marco) - things should have a role towards advancing the group. We measure our methodological assumptions on an "objective" reality based on the Q/A listed above.  We believe computer vision truths are both singular and multiple, so we focus not on methods but the importance of the questions with regards to member's meaning - defined as, the sensitive interpretation of what the group feels is important. Our methods blends rich qualitative data and quantitative methods/AI models to test our theory.
 	
## 1.3 CORNER STORE APPLICATIONS 

* Corner stores must evolve with shoppers' changing ideas of convenience. Our computer vision applications merges all the data silos -- video streams, financial records, service notes -- into a single platform.  Computer vision models are then trained on our in-house "Corner Store Social Graph" that enables each respective model to better understand the complex scenarios of each corner store. Working alongside workers the corner store applications help humans move beyond existing roles, positions and expectations into more dynamic ones. 
	* WhatYouAlmostBoughtApp >> Detect shoppers' cross product interactions to better understand product positioning strategies 
	* AutonomousCheckoutApp >> Build 'running tabs' for people as they shop along with ez payment option  

## 2 RELATED WORKS

## 3 RESEARCH GOAL

* We have tried dozens of different ways to construct a computer vision system before designing one from scratch that is both functional and manufacturable.  

## 3.1 THE SYSTEM 

* Our systems consists of a Nvidia Jetson Xavier NX and Raspberry Pi Camera V2 running NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization.

## 3.2 NETWORK PRETRAINING & DATA PREP

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across 22k categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and better balance the width and depth of the network.

## 3.3 FUSION ARCHITECTURE

## 3.4a NETWORK TRAINING

* We train our computer vision machines on our "Corner Store Social Graph" which enables us to experiment with a diverse research approaches and fine-tune our architectures to navigate uncertainity better, faster and with less computational energy.

# 3.4b CORNER-STORE-SOCIAL-GRAPH DATASET

* Bias is inevitable when training computer vision models for human action-object detections in video streams. To combat this we apply our study of member's meaning to build datasets that better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what adults feel is important. Our reality is political, but the dominant groups claim as the norm when training computer vision machines need not be.

* What is member's meaning? Generally speaking, it's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world (i.e. local knowledge, preferences, values, beliefs). Observations include the knowledge embedded in the heads of corner store staff and its regulars.  Data includes: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots and unstated goals.  Guided by this method, we hand label human-object interactions in a set of video streams, in order for the computer vision models to be able to learn what actions look like from a variety of different biases, angles, etc.  Once the models have digested these video streams, the algorithms are let loose on raw unseen corner store video streams for experiments. 

* STEP 1 DataCollection - Video Streams & Field Notes
* STEP 2 TidyDataSet - In-house hand-labeling/autonencoder makes use of collected data that are semantically similar to label human-object interactions in video streams
* STEP 3 ReproducibilityRecipe - Set up calculations in a way that promotes common data standards and portability across corner stores for better flow of data

* "Corner Store Social Graph" (v1)
	* 160 actions
	* 10 clips per actions
	* 1600 clips @ 3 - 12 seconds each
	* 30 fps
	* 640 x 480
	* Audio: YES

## 3.5 NETWORK ARCHITECTURE

## 3.6 IMPLEMENTATION

## 4 EXPERIMENTS

* In this section we explore the generalizability of networks on different benchmark datasets.

## 4.1 UCF-101 DATASET

* 13320 videos across 101 action classes

## 4.2 HMDB-51 DATASET

* 6766 videos across 51 action classes

# 4.3 CORNER-STORE-SOCIAL-GRAPH DATASET

## 5 ENSURING DATA PRIVACY

* Dr Ben Goldacre of Oxford and his colleagues May 2020 approach to studying the medical records of 17m people in Britain inspired our privacy practices.  Their team developed software that let them run analysis without copying or moving data out of that data center. Instead they poked data thru a secure connection, with a log of all queries run on the medical records to create an audit trail. Their open source methods preserved confidentiality while freeing high value information for analysis. It also gave the public a better idea about how their data is used. We designed and built our computer vision machine and its applications with this approach to privacy in mind.

## 6 DISCUSSION

## 7 SANDBOX

* Teaching computer vision applications to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs 
* Rewriting code and making arrays more ergonomic
* Determining the metrics that improve downstream performance
* Lowering the costs of switching data across different corner stores
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
* "FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks" (2016)
* "A Large Dataset to Train Convolutional Networks for Disparity, Optical Flow and Scene Flow Estimation" (2016)


