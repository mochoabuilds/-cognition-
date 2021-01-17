*** WORKING PAPER ***

*** ATTACHED CODE:  Packaged Goods Classifier - Proof of Concept ***

## 1 SUMMARY

* Advances in machine learning have given neighborhood corner stores far shinier toolkits.  This shift could spark major improvements in how corner stores run their business in the neighborhoods.  

## 1.1 INTRODUCTION

* Hyperlocal by nature, corner stores are inherently loyal to their surrounding community. Many have been known to benefit from handshake deals that let neighbors grab goods on credit. This socio-economic infrastructure can't be underestimated. Our corner stores are part pantry, part place to hug the block. They are key to safety and prosperity in your young midwestern cities.  Corner stores prescence can't be underestimated.  

* To transform the corner store toolkit, and not just its IT department, we take mature open-source software and embed it in services everyone can trust. A culture of human-centered design, test-driven development and edge-cloud operations drive our highly automated and easy-to-use applications.

## 1.2 WHY FOCUS ON CORNER STORES? 

* To win in the neighborhood corner store today, you gotta have loyal regulars.  Our technology focuses on making their checkout more simple, certain and hospitable.  My goal is take the idea of waiting in line entirely out of the equation... Walk in > tap a tile with your phone > shop > walk out

* What unique about our technology is that it accesses machine learning programs both remotely and locally rather than installing them on big old actual computers.  Instead it's done on hand sized computing devices with their own camera - so applications are highly automated, readily avaliable and easy-to-use.  Apps include: 
	* Autonomous Checkout >> System watches guests browse shelves, keeps a running tab of items taken from shelves and prompts guests with SMS payment upon exit
	* What You "AlmostBought" App >> Detect guests cross product interactions to better understand product positioning strategies 
	* Data Exchange >> Guests share and sell their data for training machine learning models

## 1.3 HOW WILL WE DO IT?

* To address our biggest challenge, the impracticality of approaching every machine learning problem with brute computing power, we looked for shortcuts. Rather than having software/edge devices see corner store scenarios thru step by step thinking, our tech sees scenarios with its own "intuition".  It learns that from translated rules of thumb that humans also lean on, but struggle to articulate. Our in-house autoencoder does the translating of these rules of thumb to make real world scenarios more understandable for our applications.  This is not our original system, but our current approach gives us more room to grow and boost our tech's accuracy further. We have tried dozens of different ways to construct an autonomous checkout system before designing this one from scratch.  
	
## 2 RELATED WORKS

## 3 METHODS


## 3.1 SYSTEM OVERVIEW

* Our system consists of an off-the-shelf camera and Jetson Xavier NX embedded computing board that runs our code using NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization.


## 3.2 DOWNLOADING OPEN SOURCE MODELS

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across thousands of  categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and helps us better balance the width and depth of the network.

## 3.3 LABELING TRAINING DATASETS

* Bias is inevitable when training machine learning models for human action-object detections in video streams. To counter this bias we build datasets for each respective corner store to better debase the dominant groups claim as the norm. Our reality is political, but the dominant groups claim as the norm when training AI applications need not be. We believe this approach helps the models better "see" the sensitive interpretations of what humans feel is important.  
* Our in-house "ethographic autoencoder" translates human rules of thumb from staff and loyal regulars into a lanugage AI models can use to "see" corner stores with their own hyperlocal "intuition".  This "intuition" will prove immensely helpful in future edge cases.

* STEP 1 >> DataCollection - Hand labeling of human rules of thumb into video streams
* STEP 2 >> TidyDataSet - In-house "ethnographic autonencoder" notices human-action interactions that are semantically similar to hand labeled human rules of thumb from previous video streams
* STEP 3 >> ReproducibilityRecipe - Set up classification calculations in a way that promotes common data standards and portability across multiple corner stores for better flow of this store-by-store "intuiton" across neighborhoods

## 3.4 CONFIGURE PLATFORMS/FILES

* VIDEO --> Capture --> Decode --> Image Processing --> 
* Stream Mgmt --> Detection --> 
* Tracking --> On Screen Display --> OUTPUT 

## 3.5 CUSTOMIZING MODEL

## 3.6 ON-SITE TESTING

## 4 EXPERIMENTAL DATA

* In this section we explore the accuracy/generalizability of models on different benchmark data sets.

## 4.1 UCF-101 DATASET

* 13320 videos across 101 action classes

## 4.2 HMDB-51 DATASET

* 6766 videos across 51 action classes

## 5 DISCUSSION

## APPENDIX: BI-DIRECTIONAL COMMUNICATIONS, ETC.

* In this section we describe how we send and recieve event triggered messages between cloud and device, request system logs and conduct model updates.

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
*


