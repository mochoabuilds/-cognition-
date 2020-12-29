*** WORKING PAPER ***

*** ATTACHED CODE:  Packaged Goods Classifier - Proof of Concept ***

## 1 SUMMARY

* Society's shift to mobile payments requires a service that makes checkout more simple and certain. Our prototypes enables corner stores/small grocers to conduct autonomous checkout for goods via SMS, with loyal regulars. This applied AI technology will spark a major improvement in how corner stores/small grocers run their business.  Our prototypes take the idea of waiting in line entirely out of the equation.  Society's shift to mobile payments, plus our code/magic will create a network effect among partnering corner stores, making our service the simpliest and most certain way to pay in person. 

## 1.1 INTRODUCTION

* Corner stores - 1 part pantry, 1 part place to hug the block. Their prescence can't be underestimated.  Hyperlocal by nature, corner stores are inherently loyal to its surrounding folk. Many have been known to benefit from handshake understandings that let them grab goods on credit. This socio-economic infrastructure can't be underestimated, it's key to safety and prosperity in our young Midwestern cities. 

## 1.2 WHY FOCUS ON CORNER STORES? 

* To win in the corner store market today, you gotta build loyal regulars.  Its hyperlocal nature means word of a better automated experience will go around quickly.

* What unique about our service is that it accesses AI programs remotely rather than installing them on actual computers - so applications are highly automated, readily avaliable and easy-to-use.  Sample apps include: 
	* Autonomous Checkout App >> Watch shoppers browse shelves, keep a running tab of items taken from shelves and prompt shoppers with SMS payment option upon exit
	* What You "AlmostBought" App >> Detect shoppers' cross product interactions to better understand product positioning strategies 
	* Data Exchange >> Shoppers share and sell their data for training AI models

## 1.3 HOW WE DO IT?

* A culture of test-driven development, human-centered design and edge-cloud operations drive our theory and methods. Our mixed methods approach blends rich ethnographic data from humans with powerful AI models to create a portfolio of services that are highly automated and easy-to-use. To transform the corner store, and not just its IT department, our approach takes mature open-source software and embeds it in services everyone can trust. Our long term goal is to help corner stores/small grocers run AI applications that make checkout more simple and certain.
	
## 2 RELATED WORKS

## 3 THEORY + METHODS

* To address our biggest challenge - the impracticality of approaching every AI problem with brute computing power - we looked for shortcuts. Rather than having AI models see corner store scenarios via step by step thinking, our AI models see these scenarios with their own "intuition" learned from many many translated rules of thumb that humans also lean on, but struggle to articulate. We translated them with an in-house autoencoder to make more functional and understandable for our models.
* This is not our original system, but our current approach gives us more room to grow and boost the technology's accuracy further. We have tried dozens of different ways to construct a AI/computer vision system before designing this one from scratch.  

## 3.1 SYSTEM OVERVIEW

* Our system consists of an off-the-shelf camera and Jetson Xavier NX embedded computing board that runs our code/magic using NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization.

## 3.2 UPLOADING/PRETRAINING NETWORK

* We use an offshoot of ImageNet model to pretrain our multi-stream network. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across ~22k categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and helps us better balance the width and depth of the network.

## 3.3 COLLECTING TRAINING DATA ("ETHNOGRAPHIC AUTOENCODER")

* Bias is inevitable when training computer vision models for human Action-Object detections in video streams. To mitigae this we build our dataset for each respective corner store/small grocer to better debase the dominant groups claim as the norm. Our reality is political, but the dominant groups claim as the norm when training AI models need not be. We believe this approach helps models better "see" the sensitive interpretations of what humans feel is important.  An in-house "ethographic autoencoder" translates ethnographic field notes & human rules of thumb from staff and loyal regulars of each space into a lanugage AI models can use to "see" corner stores with their own hyperlocal "intuition".  This "intuition" will prove helpful in edge cases.

* STEP 1 >> DataCollection - Video Streams & Hand Labeling 
* STEP 2 >> TidyDataSet - In-house "ethnographic autonencoder" makes use of collected field data that are semantically similar to more robustly label human-object interactions in video streams
* STEP 3 >> ReproducibilityRecipe - Set up classification calculations in a way that promotes common data standards and portability across multiple corner stores for better flow of shopper data

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


