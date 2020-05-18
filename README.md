Human-Computer Vision:  Computational Models and Ethnography (2020)

By Michael Valentino Ochoa et la.


INTRODUCTION 

- In this paper, we explore our methods for understanding scene recognition in human-computer vision. In Part I, we present an ethnographic study showing the natural scene categorization of a neighborhood market. In Part II, we study what human subjects perceive when they glance at images of a neighborhood market. In Part III, a computer vision model characterizes natural scene properties of a neighborhood market to understand their origins.  Finally in Part IV, we show how natural scene categorization with data from Part I, II and III could be dropped into a hierarchical Bayesian model to gain a deeper sense of what a pleasurable neighborhood shopping experience can be.

MOTIVATION

- What sort of influence do we want computer vision algorithms to have over our life? 
- What will keep the neighborhood market ahead of competition in a changing world?

LITERATURE REVIEW & CONTRIBUTION

HUMAN-COMPUTER VISION 

	PART I  ETHNOGRAPHIC RESEARCH

    - Qualitative research is driven by firsthand participation in once unfamiliar social circles to pull a sense of what’s relevant in that world.  For the purpose of this research we visit our neighborhood mart (Location:  Middle East Mart - Andersonville, Chicago).

	PART II  QUICK-LOOK PERCEPTIONS

	— Human takes quick glances at an image.  Questions about image follow.

	PART III  COMPUTER VISION MODEL OVERVIEW
    * Who is here? // Human pose estimation
    * Whatcha up to? // Action recognition
    * Who has what? // Temporal association
    * What is it? // Object classification
    * Whose hands are doing what, with what object? // Action analysis 

	PART IV  PRODUCT DESIGN

	Five different design cases for our embedded computer vision device.  

OK! LET'S GET STARTED!

01 Installing Required Packages and Libraries
* Python
* OpenCV https://opencv.org/
* scikit-image https://scikit-image.org/ & scikit-learn https://scikit-learn.org/stable/index.html
* dlib http://dlib.net/
* Keras https://keras.io/ & Tensorflow https://www.tensorflow.org/
* Caffe http://caffe.berkeleyvision.org/
* Configuring Raspberry Pi

02 Accessing RPi Camera
Qui dolorem ipsum, quia dolor sit amet consectetur adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem

EXPERIMENTS AND RESULTS

DISCUSSION 

CURRENT CHALLENGES
* Handling constant partial and full occlusions
* Branching object persistence models across multiple cameras
* Restructuring the code to Rustic
* Navigating open source software support
* Determining the metrics that improve downstream performance
* Handling frequently changing databases schema, data types and complex objects
* Handling the velocity of vision data across different frequencies
* Bridging the edge-cloud barrier for real time computer vision analytics in the cloud 

BIBLIOGRAPHY
