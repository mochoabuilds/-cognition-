*** WORKING PAPER ***

*** ATTACHED CODE:  Packaged Goods Classifier - Proof of Concept ***

## 1 INTRODUCTION

* Corner stores do more than just provide us with essential goods. They're where unrelated people relate. They're somewhere you can go for the simple pleasure of good conversation. Its social infrastructure is key to safety and prosperity in our Midwestern cities. Tho corner stores are in a once-in-a-generation shift as cloud/mobile technology becomes more baked into everyday life. To help out, our research deploys computer vision technology to make corner stores more simple and certain. We master the art of building software corner stores love - and use our portfolio of applications to run it the edge-cloud.

## 1.1 HOW WE DO THIS?

* To transform the corner store, not just its IT, you must invest both in people and technology. A culture of test-driven development, human-centered design and edge-cloud native operations must be the norm. Products must also be highly automated and easy to use. Our technologies must spark major improvements in how corner stores run their business. A partnership with our research group means being led through the next stage of their corner store. We help corner store run computer vision application where they want and scale them across targets. Our approach takes mature open-source software and embeds it into applictions you can trust.
	
## 1.2 WHY FOCUS ON CORNER STORES? 

* To win in the corner store market today, things should have a role towards advancing the group. We mesaure this on an objective basis with field observation guided by Q/A listed below. We believe corner store applications must reflect the sensitive interpretation of what the corner store community feels is important. Our approach blends rich qualitiative data and AI models to test our theory of how the corner store could win. that revolves around de-basing the dominant group's claims as the norms for life when building computer vision models.

* Field Observation Q/A used to encode/decode the world:
	* "how many?" "is there?"  (descriptive questions)
	* "what is responsible for...?" (explanatory questions)
	* "what will happen?" (predictive questions)
	* "what if?" (counterfactual questions)
	* "members meaning" (rich qualitative questions)
	*  temperature, sound levels, smells (sensory impressions)
	
* Data is collected on a store-by-store basis and used to build a Corner-Store-Social-Graph 

*
 	
## 1.3 CORNER STORE APPLICATIONS 

* Corner stores must evolve with shoppers' changing ideas of convenience. Our applications merges all data silos -- video streams, financial records, service notes -- into a single platform.  
	* WhatYouAlmostBoughtApp >> Detect shoppers' cross product interactions to better understand product positioning strategies 
	* AutonomousCheckoutApp >> Build 'running tabs' for people as they shop along with ez payment option  

## 2 RELATED WORKS

## 3 RESEARCH GOAL

* We have tried dozens of different ways to construct a computer vision system before designing one from scratch that is both functional and manufacturable.  

## 3.1 THE SYSTEM 

* Our systems consists of a Nvidia Jetson Xavier NX and Raspberry Pi Camera V2 or Logitech c270 Webcam running NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization.

## 3.2 NETWORK PRETRAINING 

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across 22k categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and better balance the width and depth of the network.

## 3.3 FUSION ARCHITECTURE

## 3.4 NETWORK TRAINING WITH CORNER-STORE-SOCIAL-GRAPH

* We train our computer vision machines on our "Corner Store Social Graph" which enables us to experiment with a diverse research approaches and fine-tune our architectures to navigate uncertainity better, faster and with less computational energy.

* Bias is inevitable when training computer vision models for human action-object detections in video streams. To combat this we apply our rich field research towards building datasets that better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what adults feel is important. Our reality is political, but the dominant groups claim as the norm when training computer vision machines need not be. Our rich field research includes the knowledge embedded in the heads of corner store staff and its regulars.  Data includes: personal interviews, sensory impressions, neighborhood idiosyncrasies, blind spots and unstated goals.  
* Guided by our mixed-method approach, we hand label (encode) human-object interactions in a set of video streams, in order for the computer vision models to be able to learn what actions look like (decode) from a variety of different biases, angles, etc.  Once the models have digested these video streams, the algorithms are let loose on corner store video streams for classification accuracy experiments.

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


