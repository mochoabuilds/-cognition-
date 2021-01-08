*** WORKING PAPER ***

*** ATTACHED CODE:  Packaged Goods Classifier - Proof of Concept ***

## 1 SUMMARY

* Advances in machine learning have given corner stores a far shinier array of tools.  Along other great minds, we test whether an algorithm could enable corner stores to conduct autonomous checkout with loyal regulars. Our technology will spark a major improvement in how corner stores run their business.  We take the idea of waiting in line entirely out of the equation and make corner store checkout more simple, certain and hospitable.

## 1.1 INTRODUCTION

* Corner stores - part pantry, part place to hug the block. Their prescence can't be underestimated.  Hyperlocal by nature, corner stores are inherently loyal to their surrounding community. Many people been known to benefit from handshake deals that let them grab goods on credit. This socio-economic infrastructure can't be underestimated, it's key to safety and prosperity in our young Midwestern cities. 

## 1.2 WHY FOCUS ON CORNER STORES? 

* To win in the corner store market today, you gotta have loyal regulars.  Our technology focuses on making them more simple, certain and hospitable.

* What unique about our service is that it accesses machine learning programs remotely rather than installing them on actual computers - so applications are highly automated, readily avaliable and easy-to-use.  Applications include: 
	* Autonomous Checkout >> Watch shoppers browse shelves, keep a running tab of items taken from shelves and prompt shoppers with SMS payment upon exit
	* What You "AlmostBought" App >> Detect shoppers' cross product interactions to better understand product positioning strategies 
	* Data Exchange >> Shoppers share and sell their data for training machine learning models

## 1.3 HOW WE DO IT?

* To transform the corner store, and not just its IT department, we take mature open-source software and embed it in services everyone can trust. A culture of human-centered design, test-driven development and edge-cloud operations drive our highly automated and easy-to-use services.
	
## 2 RELATED WORKS

## 3 THEORY + METHODS

* To address our biggest challenge, the impracticality of approaching every machine learning problem with brute computing power, we looked for shortcuts. Rather than having software/hardware see corner store scenarios thru step by step thinking, our technology sees scenarios with its own "intuition" learned from translated rules of thumb that humans also lean on, but struggle to articulate. Our in-house autoencoder translates these rules of thumb to make more functional and understandable for our software.
* This is not our original system, but our current approach gives us more room to grow and boost our technology's accuracy further. We have tried dozens of different ways to construct an autonomous checkout system before designing this one from scratch.  

## 3.1 SYSTEM OVERVIEW

* Our system consists of an off-the-shelf camera and Jetson Xavier NX embedded computing board that runs our code/magic using NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization.

## 3.2 UPLOADING/PRETRAINING NETWORK

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across ~22k categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and helps us better balance the width and depth of the network.

## 3.3 COLLECTING TRAINING DATA ("ETHNOGRAPHIC AUTOENCODER")

* Bias is inevitable when training autonomous checkout models for human action-object detections in video streams. To mitigae this we build datasets for each respective corner store to better debase the dominant groups (i.e. software engineers) claim as the norm. Our reality is political, but the dominant groups claim as the norm when training autonomous checkout models need not be. We believe this approach helps models better "see" the sensitive interpretations of what humans feel is important.  Our in-house "ethographic autoencoder" translates human rules of thumb from staff and loyal regulars into a lanugage machine learning models can use to "see" corner stores with their own hyperlocal "intuition".  This "intuition" proves immensely helpful in edge cases.

* STEP 1 >> DataCollection - Video Streams & Hand Labeling 
* STEP 2 >> TidyDataSet - In-house "ethnographic autonencoder" makes use of collected field data that are semantically similar to more robustly label human-object interactions in video streams
* STEP 3 >> ReproducibilityRecipe - Set up classification calculations in a way that promotes common data standards and portability across multiple corner stores for better flow of shopper data

## 3.4 ADDING NETWORK LAYERS

## 3.5 TRAINING THE MODEL

## 3.6 TESTING THE MODEL

## 4 EXPERIMENTS

* In this section we explore the accuracy/generalizability of machine learning models on different benchmark data sets.

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


