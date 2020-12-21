*** WORKING PAPER ***

*** ATTACHED CODE:  Packaged Goods Classifier - Proof of Concept ***

## 1 INTRODUCTION

* Corner stores - part pantry, part place to hug the block. Their prescence can't be underestimated.  Hyperlocal by nature, corner stores are inherently loyal to its neighborhood inhabitants. Some locals have been known to benefit from understandings that let them grab essential on credit. There may be chaos outside, but the corner store brings a calming stability in these times. They're also where unrelated people relate. Its socio-economic infrastructure is key to safety and prosperity in our young Midwestern cities. 
* Tho corner stores are in a once-in-a-generation shift as cloud/mobile services becomes more baked into everyday life. To help them, our research deploys AI technology to spark major improvements in how corner stores run their business.


## 1.1 HOW WE DO THIS?

* To transform the corner store, not just its IT department, our approach takes mature open-source software and embeds it into applications everyone can trust. Our mixed methods approach blends rich qualitative data from humans with AI models to create a portfolio of services that are highly automated and easy-to-use. A culture of test-driven development, human-centered design and edge-cloud operations drive our methods. We strive to help corner stores run applications that make services more simple, certain and scalable.  
* To address our biggest challenges, the impracticality of approaching every problem with brute computing power.  It soon became clear that the move is to look for shortcuts.  Rather than having our AI models see corner store scenarios as step by step thinking, models see scenarios with their own "intuition" learned from many translated examples of rules of thumb humans also use, but struggle to articulate. To be honest, we understand AI is a box of many different tools, and this is not our original system, but this new approach gives us more room to grow and boost the software's accuracy further.

	
## 1.2 WHY FOCUS ON CORNER STORES? 

* To win in the corner store market today, you gotta build loyal regulars.  Its hyperlocal nature means word of a new, simplier and easier corner store experience will go around quickly.  Our technology means spaces become more than just a store, they become extensions of the home for shoppers. This feeling can't be underestimated.

* Right now we are trying to extend software-as-a-service -- by accessing AI programs remotely rather than installing on them office computers -- particularly for corner store applications that are highly automated, easy-to-use and readily avaliable.
	* Autonomous Checkout App >> Match the technological and operational plumbing of this service to its new reality
	* WhatYouAlmostBought App >> Detect shoppers' cross product interactions to better understand product positioning strategies 
	* Data Exchange >> shoppers share and sell their data for training computer vision models

## 2 RELATED WORKS

## 3 RESEARCH GOAL

* We have tried dozens of different ways to construct a AI/computer vision system before designing this one from scratch.  It is both functional and manufacturable.  

## 3.1 SYSTEM 

* Our systems consists of a Nvidia Jetson Xavier NX and Raspberry Pi Camera V2 or Logitech c270 Webcam running NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization.

## 3.2 NETWORK PRETRAINING 

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across 22k categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and better balance the width and depth of the network.

## 3.3 FUSION ARCHITECTURE

## 3.4 CORNER-STORE-SOCIAL-GRAPH TRAINING

* We train our AI/computer vision models on the "Corner Store Social Graph" to experiment and fine-tune our architectures to operate with higher accuracy and less computational power.

* Bias is inevitable when training computer vision models for human action-object detections in video streams. To combat this we apply our rich Q/A towards building datasets that better debase the dominant groups claim as the norm.  This helps our computer vision models better "see" the sensitive interpretations of what adults feel is important. Our reality is political, but the dominant groups claim as the norm when training computer vision machines need not be. Our field research is made up of the rules of thumb embedded in the heads of corner store staff and its regulars.
* Guided by our mixed-method approach, we hand label (encode) human-object interactions in a set of video streams, in order for the computer vision models to be able to see scenarios with their own "intuition". We then use those translated rules of thumb to make decisions (decode) from a variety of different biases, angles, etc. 
* Once the models have digested these video streams, the classifications algorithms are let loose on corner store video streams for various accuracy/generalizability experiments. 

* STEP 1 >> DataCollection - Video Streams & Hand Labeling 
* STEP 2 >> TidyDataSet - In-house hand-labeling/autonencoder makes use of collected data that are semantically similar to label human-object interactions in video streams
* STEP 3 >> ReproducibilityRecipe - Set up classification calculations in a way that promotes common data standards and portability across multiple corner stores for better flow of data

* "Corner Store Social Graph" (v1)
	* 160 actions
	* 10 clips per actions
	* 1600 clips @ 3 - 12 seconds each
	* 30 fps
	* 640 x 480
	* Audio: YES

## 3.5 SYSTEM ARCHITECTURE

## 3.6 NETWORK ARCHITECTURE

## 3.7 IMPLEMENTATION

## 4 EXPERIMENTS

* In this section we explore the accuracy/generalizability of AI models on different benchmark data sets.

## 4.1 UCF-101 DATASET

* 13320 videos across 101 action classes

## 4.2 HMDB-51 DATASET

* 6766 videos across 51 action classes

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
* Better understanding how social, economic and legal systems work together to achieve research goals 

## APPENDIX A: POLICY MEMORANDUM

* The introduction of modern, legally enforceable computer vision privacy rights will be politically fraught.  Reform must keep up the long, hard slog of countering implicit bias, cementing privacy rights and building the infrastructure to uphold them. Those building computer vision applications must accept greater responsiblity for its future. We must be part of setting the agenda, attitute, culture and laws around computer vision privacy rights.

## ACKNOWLEDGEMENTS

* This work was supported by my lovely partner K, my immediate family, my close friends and confidants and the open source community. 

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


