*** "Deep Learning Based Actionable Credit System for Cashierless Checkout"

*** Attached Code:  Proof of Concept -- Packaged Goods Classifier 

## 1 CIRCUMSTANCES OF CONCEPTION

* During Spring 2020, I visited my neighborhood corner store in Chicago.  My plan was to scoop some essentials.  Soon I found myself in a line that snaked up and down the aisles as I maintained physical distance on account of COVID-19 restrictions.  Yet the line continued to grow and I was now in a standing among many unmasked people, as they gifted and gabbed.  Aerosols were plentiful.  After a few anxious minutes I left, immediately thinking there must be a better, clearer and more hospitable way for customers (especially regulars) to do checkout.  

## 1.1 MARKET CONTEXT

* Advances in machine learning have given corner stores far shinier toolkits.  Tools have gotten smaller, parallelised and now run along with smartphones, progress has become very fast. As AI domain knowledge roots itself, it could spark major improvements in how corner stores run their business.  This research functions as a mediator for emerging tools that make corner store checkout simplier, clearer and more hospitable. Perhaps 

## 1.2 PURPOSE / PROBLEM SOLVED

* Hyperlocal by nature, corner stores are inherently loyal to their surrounding neighborhood. Many souls been known to benefit from handshake deals that let them grab goods on credit. This socio-economic infrastructure can't be underestimated. A good corner store's prescence can't be underestimated.  To transform the corner store toolkit, and not just its IT department, we take mature open-source software and embed it in services everyone can trust. Our system assembles all the knowledge scattered throughout the corner store and translates it into tools that corner stores might not otherwise realized were possible.

## Our tools revolve around the idea that: people don't want to make payments, they want to do what a payment facilitates. 

* Some regulars want the option to grab goods on credit and simply skip the line entirely.  They want their corner store to be part pantry & part place to say hello.  Such spaces are key to safety and prosperity in your young midwestern cities.  We offer interested regulars an intelligent AI solution that makes for a simplier, clearer and more hospitable checkout experience.

## Walk in > Tap a tile > Shop > Walk out 

* What's unique about our approach is that it accesses AI programs both remotely and locally. This more decentralized approach reduces the amount of data transmitted and thus the amount avaliable to intercept or jam.  Rather than installing algorithms on big old actual computers, computation @ inference time is done on hand sized computing devices equipped with their own cameras.  Tools/apps are highly automated, readily avaliable and easy-to-use/modify.  Prototypes include:
	* Autonomous Checkout >> System watches guests browse shelves, keeps a running tab of items taken from shelves and prompts guests with SMS 'actionable credit' upon exit
	* What You "AlmostBought" App >> Detect guests cross product interactions to better understand product positioning strategies 
	* Data Exchange >> Guests share and sell their data for training AI models

## 1.3 MOTIVATIONS

* To address our biggest challenge, the impracticality of approaching every AI problem with brute computing power, we looked for shortcuts. Instead of than having our camera, system and models see corner store scenarios via step by step thinking, ours sees scenarios with its own "intuition".  Seeds used to plant this idea in include helping the system understand that human actions are more complex that just identifying objects alone, because it requires intuition - a "human understanding" of humans interact with objects, human poses at difference angles, scene context.  Most importantly, how hospitable shopping experiences happen among humans.

## These challenges motivate us to study two problems: 1) how to design an effective video-framework for learning corner store representations in long-range temporal structures 2) how to extend this design to better capture guest yearnings
	
## 2 RELATED WORKS

## 3 SYSTEMS OVERVIEW / METHODS

* Our system consists of an off-the-shelf camera and Jetson Xavier NX embedded computing board that runs our code using NVIDIA's JetPack SDK for libraries, APIs, debugging and optimization. The goal is to create a 'digital twin' of a corner store that integrates real-time data from off-the-shelf cameras to display the state of the shop at any given time, and extend that understanding towards autonomous checkout.  Using off-the-shelf cameras, embedded computing boards and AI models our system learns to understand guest behaviors and preferences at any given time. 

* BLOCK DIAGRAM OF CENTRAL SYSTEM

* The computing board is optimized using NVIDIA's Metropolis framework to performs real-time computations of AI algorithms on the edge.  This system tests and measures the success of checkout accuracy (%) and extends these valuable insights to corner stores across the system.

## 3.1 DOWNLOAD OPEN SOURCE MODELS ("PRETRAINING")

* We use an offshoot of ImageNet model to pretrain our  AI model. We are immensely grateful for ImageNet and the human labor it took to sort, label and prep the millions of images across thousands of categories. Pretraining allows us to avoid representational bottlenecks, boost our activations per tile and helps us better balance the width and depth of the network.

# 3.2 CORNER STORE v-1 DATASET

* The dataset is focused on corner store scenarios  Action classes cover:  human actions, human-object interactions.  Many actions require temporal reasoning to differentiate, for example a door opening vs door closing.  Other actions need more focus on the object for classification, such as browsing shelves for different goods. The dataset has 100 action classes, with 100 clips for each action. Each clip runs approx 10 seconds.  The current dataset has 10,000 videos, split three ways -- one for training, one for validation and one for testing. Clips comes from in-house data collection and have variable resolution and frame rates.

* Full class list of how a hospitable shopping experience happens among humans is posted in the Appendix, with parent child groupings.

## 3.3 DEEP DATA PREP

* Bias is inevitable when training machine learning models for human action-object detections in video streams. To counter this each respective corner store is made the center of their initial training data, to better debase the dominant groups claim as the norm for theories about how guests shop / leavier happier in that store. Our reality is political, but the AI developer perspective as the norm when training AI applications need not be. We believe this approach helps the models better "see" the sensitive interpretations of what humans feel at each respective corner store is important.

* AI models rely on an autoencoder to understand translated rules of thumb about how people shop and leave happy that humans also lean on, but struggle to articulate. Our in-house autoencoder makes sense of our human ethnographic field notes as labeled vectors to better understand high level vision concepts as interacting objects, human poses and scene context. 

## Our in-house autoencoder compresses human rules of thumb/labels/vectors from staff and loyal regulars into short binary codes that AI models use to "see" corner stores with their own hyperlocal "intuition". This "intuition" helps AI models generalize to longer sequences than those seen during training.  It also helps us combine several store datasets to learn neighborhood level human-object representations, and easily add rich training data on the fly.  This deep data prep gives us more room to grow and boost our technology's accuracy and lower our computational budget.

* FLOWCHART

* 1 >> DataCollection - Hand labeling of human rules of thumb into video streams
* 2 >> TidyDataSet - In-house "ethnographic autonencoder" notices human-object interactions that are semantically similar to hand labeled human rules of thumb from previous video streams
* 3 >> ReproducibilityRecipe - Set up classification calculations in a way that promotes common data standards and portability to decrease overfitting models.

## 3.4 ARCHITECTURES

* Inspired by the human visual cortex, our model contains two pathways the ventral (shape and color of objects) and the dorsal (caused by motion of objects).  This network architecture helps us represent motion using the optical flow displacement field.  A two stream approach also helps the model better understand how repetitive actions such as "doors opening/closing" require an understanding of different spatiotemporal cues at different scales.

* DRAWING

## 3.5 TRAINING DETAILS

* Learning Rates 
* Additional Data Prep
* Testing

* BLOCK DIAGRAM OF SERVER COMPONENTS

## 4 EXPERIMENTS

* In this section we explore the accuracy/generalizability of models on different benchmark data sets. 

## 4.1 IMPLEMENTATION DETAILS

* BLOCK DIGRAM OF SOFTWARE MODULES WITHING HARDWARE

## 4.2 RESULTS

## 4.3 COMPARISONS

* UCF-101 DATASET - 13320 videos across 101 action classes
* 4.2 HMDB-51 DATASET - 6766 videos across 51 action classes

## 5 DISCUSSION

## APPENDIX: "CORNER STORE v-1" DATASET ~ 100 ACTION CLASSES

* In no particular order: "Running" "Throwing" "Eating X" "Drinking X" "Dancing" "Attacking" "Touching X" "Crawling" "Sweeping Floor" "Checking X" "Reogranizing X" "Carrying Child" "Other Payment" "Leaving Store" "Entering Store" "Following Down" "Garbage Collection" "Hugging" "Bending Down for X" "Mapping" "Opening X" "Picking X From Shelf Z" "Playing Catch" "Pumping Fist" "Pushing Cart" "Pushing Stroller" "Dancing" "Shaking Hands" "Sign Language Interpreting" "Slapping Person" "Big Sneeze" "Sword Fighting" "Tasting X" "Tickling" "Unboxing" "Applauding" "Clapping" "Mopping Floor" "Cleaning Windows" "Petting Dog" "Punching Person" "Pushing Wheelchair" "Roller Skating" "Washing Hands" 


## ACKNOWLEDGEMENTS

* This work was supported by my lovely partner K, my immediate family, my close friends and confidants and the open source community. 

## SANDBOX

* Teaching computer vision applications to NOT use guest biometrics as a condition of accepting payment under the Song Beverley Act of 1971
* Better understanding the front-back orientation of human limbs due to clothing, lighting, background, optical interference
* Bridging the edge-cloud barrier to lower server costs 
* Rewriting code and making arrays more ergonomic
* Determining the metrics that improve downstream performance
* Lowering the costs of switching data across different corner stores
* Better understanding how social, economic and legal systems work together to achieve research goals 

## REFERENCES

* Deep Learning, An MIT Press Book (2016)
* Writing Ethnographic Field Notes, 2nd Edition (2011)
* The Great Good Place by Roy Oldenburg (1989)
* Interaction of Color by Josef Albers (1963)
*
* "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset" (2018)
* "Two-Stream Convolutional Networks for Action Recognition in Videos" (2014)
* "FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks" (2016)
* "Spatiotemporal Residual Networks for Video Action Recognition" (2016)
* "Deep Residual Learning for Image Recognition" (2015)
* "Towards Good Practices for Very Deep Two-Stream ConvNets" (2015)
* "Temporal Segment Networks: Towards Good Practices for Deep Action Recognition" (2016)

* 
*
*



