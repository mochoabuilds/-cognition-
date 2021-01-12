*** WORKING PAPER ***

*** ATTACHED CODE:  Packaged Goods Classifier - Proof of Concept ***

## 1 SUMMARY

* Advances in machine learning have given neighborhood corner stores far shinier toolkits.  The test is whether algorithms could enable corner stores to conduct autonomous checkout. I believe this shift could spark major improvements in how corner stores run their business.  My goal is take the idea of waiting in line entirely out of the equation and make checkout more simple, certain and hospitable.

## 1.1 INTRODUCTION

* Hyperlocal by nature, corner stores are inherently loyal to their surrounding community. Many have been known to benefit from handshake deals that let them grab goods on credit. This socio-economic infrastructure can't be underestimated. Corner stores are part pantry, part place to hug the block. They are key to safety and prosperity, in our historically speaking, young midwestern cities.  Corner stores prescence can't be underestimated.  

## 1.2 WHY FOCUS ON CORNER STORES? 

* To win in the neighborhood corner store market today, you gotta have loyal regulars.  Our technology focuses on making their checkout more simple, certain and hospitable.

* What unique about our technology is that it accesses machine learning programs both remotely/locally rather than installing them on big old actual computers, instead it's done on hand sized edge computing devices with its own camera - so applications are highly automated, readily avaliable and easy-to-use.  Apps include: 
	* Autonomous Checkout >> System watches guests browse shelves, keeps a running tab of items taken from shelves and prompts guests with SMS payment upon exit
	* What You "AlmostBought" App >> Detect guests cross product interactions to better understand product positioning strategies 
	* Data Exchange >> Guests share and sell their data for training machine learning models

## 1.3 HOW WE DO IT?

* To transform the corner store, and not just its IT department, we take mature open-source software and embed it in services everyone can trust. A culture of human-centered design, test-driven development and edge-cloud operations drive our highly automated and easy-to-use applications.
	
## 2 RELATED WORKS

## 3 THEORY + METHODS

* To address our biggest challenge, the impracticality of approaching every machine learning problem with brute computing power, we looked for shortcuts. Rather than having software/edge devices see corner store scenarios thru step by step thinking, our tech sees scenarios with its own "intuition".  It learns that from translated rules of thumb that humans also lean on, but struggle to articulate. Our in-house autoencoder does the translating of these rules of thumb to make real world scenarios more understandable for our applications.
* This is not our original system, but our current approach gives us more room to grow and boost our tech's accuracy further. We have tried dozens of different ways to construct an autonomous checkout system before designing this one from scratch.  

## 3.1 SYSTEM OVERVIEW

* Our system consists of an off-the-shelf camera and Jetson Xavier NX embedded computing board that runs our code using NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization.

## 3.2 UPLOADING/PRETRAINING NETWORK

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across thousands of  categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and helps us better balance the width and depth of the network.

## 3.3 COLLECTING TRAINING DATA ("ETHNOGRAPHIC AUTOENCODER")

* Bias is inevitable when training autonomous checkout models for human action-object detections in video streams. To mitigate this we build datasets for each respective corner store to better debase the dominant groups (i.e. AI developers) claim as the norm. Our reality is political, but the dominant groups claim as the norm when training AI applications need not be. We believe this approach helps the models better "see" the sensitive interpretations of what humans feel is important.  
* Our in-house "ethographic autoencoder" translates human rules of thumb from staff and loyal regulars into a lanugage AI models can use to "see" corner stores with their own hyperlocal "intuition".  This "intuition" will prove immensely helpful in future edge cases.

* STEP 1 >> DataCollection - Hand labeling of human rules of thumb into video streams
* STEP 2 >> TidyDataSet - In-house "ethnographic autonencoder" notices human-action interactions that are semantically similar to hand labeled human rules of thumb from previous video streams
* STEP 3 >> ReproducibilityRecipe - Set up classification calculations in a way that promotes common data standards and portability across multiple corner stores for better flow of this store-by-store "intuiton" across neighborhoods

## 3.4 ADDING NETWORK LAYERS

## 3.5 TRAINING THE MODEL

## 3.6 TESTING THE MODEL

## 4 EXPERIMENTS

* In this section we explore the accuracy/generalizability of machine learning models on different benchmark data sets.

## 4.1 UCF-101 DATASET

* 13320 videos across 101 action classes

## 4.2 HMDB-51 DATASET

* 6766 videos across 51 action classes

## 5 DISCUSSION

## 6 SANDBOX

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


