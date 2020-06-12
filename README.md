Hardware and Software Improvements for a Distributed Computer Vision Application (Ochoa et la., 2020)

*** WORKING PAPER ***

## INTRODUCTION
+ Hi there! I've long been puzzled by neighborhood markets (i.e. corner stores, small grocers, bodegas) — especially their checkout process! I often ask myself, could it be simpler? I dug deeper to discover the nature of the system.
+ First hand experience eventually had me hypothesizing that **IF you were to automate the checkout process THEN staff would be free to perform the kind of human associations key to healthy neighborhoods**. Examples include: 1) chatting with customers for no specific purpose 2) being the public characters that “keep an eye” on the neighborhood 3) being a “port of entry" for newcomers 4) other duties.  
+ This paper dives into the engineering and science of an autonomous checkout system. I use a mixed methods approach built upon ethnography, quick look perceptions and open source code. This distributed computer vision application scans the room with an off-the-shelf camera to understand the scene and syncs specific points in the space with connected actions. This setup helps trim computational costs by taking action only when a person comes in contact with a specific space or object.  
+ When extended to a neighborhood market this distributed setup makes autonomous checkout possible.  Customers browse goods, build their baskets and upon exit our system issues a bill to a customer via SMS, allowing customers to pay thru their own mobile payment system.

## TIMELINE
+ Winter 2018 — Spring 2020 
    + Conceptualizing & Design
+ Summer 2020 
    + People/Footfall Counter 
    + Gesture Recognition and Object Classification of Neighborhood Market Scenes
+ Fall 2020 
    + Pilot Product:  Customers browse goods, build their baskets and upon exit our system issues a bill to a customer via SMS, allowing customers to pay thru their own mobile payment system

## HOW WE APPROACH DATA PRIVACY.  WHY?
+ **Proprietors of neighborhood market ask questions about their video data thru a secure pipeline, and a public log of all queries the proprietors runs is recorded — thus the watchers themselves are watched**.   We transform a customer's actions/ data into an active piece of infrastructure underpinning their privacy.
+ We believe democracy is more likely to thrive when citizens have good information.  By baking strong privacy practices into our autonomous checkout system we hope to incentivize citizens to shop neighborhood markets more to cut their emissions, thus ensuring the shift to less carbon happens in the most efficient way possible.  

## OUR MIXED METHODS APPROACH
ETHNOGRAPHY
+ What is ethnographic research? It is firsthand participation in once unfamiliar social circles to pull a sense of what’s relevant in that world. For the purpose of this research we frequent neighborhood markets in Chicago’s Uptown and Edgewater neighborhoods.
+ Field Notes

QUICK LOOK GLANCES
+ What are quick look glances?
+ Field Notes

COMPUTER VISION
+ **We train a distributed computer vision model to understand “whose hands are doing what, with what object” in neighborhood markets scenarios**. Algorithms divide images into regions, bounding boxes and probabilities that are then integrated into more abstract and analytical efforts (i.e. mixture density network) to help machines understand the local realities that make things work elsewhere but not here.  

+ A. Human Pose Estimation | Who’s here? ![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)
+ B. Gesture Recognition | Whatcha up to? 
+ C. Object Classification | Whatcha holdin? 
+ D. Temporal Association | Who has what? 
+ E. Action Analysis Based on Location 

MIXTURE DENSITY NETWORK (MDN)
+ What is a mixed density network?
+ Model
+ Network Architecture
+ Optimization

## DISTRIBUTED COMPUTER VISION PIPELINE

+ VideoNode <—> VideoHub <—> Librarian <—> UI/UX

+ VideoNode for parameter tuning to optimize detection
+ VideoHub for logging video and event message, acknowledging
+ Librarian for extracting features from video, creates summaries and reports
+ UI/UX for SMS, mobile payment integration 

## BUILDING THIS COMPUTER VISION APPLICATION
01 Installing Required Packages and Libraries
+ Python
+ OpenCV https://opencv.org/

02 Configuring Edge Computing Device
+ Prep
+ Code
+ Notes

03 Open CV Crash Course
+ Prep
+ Code
+ Notes
+ Privacy Concerns:

04 Installing Required Packages and Libraries
+ scikit-image https://scikit-image.org/
+ scikit-learn https://scikit-learn.org/stable/index.html
+ Numpy https://numpy.org/install/
+ dlib http://dlib.net/
+ Keras https://keras.io/
+ Tensorflow https://www.tensorflow.org/
+ Caffe http://caffe.berkeleyvision.org/

05 Footfall/People Counter
+ Prep
+ Geometric Center Tracking Algorithm
+ Implementation
+ Deploying
+ Notes
+ Privacy Concerns

06 Human Pose Estimation with Tensorflow and Caffe | Who’s here?

07 Training and Deploying Custom Gesture Recognition Model | Whatcha up to?

08 Training and Deploying Custom Objects Classifier | Whatcha holdin?

09 Temporal Association | Who has what?

10 Action Analysis Based on Location

11 SMS Mobile Payments 

## EXPERIMENTS AND RESULTS
+ Datasets and Protocols
+ Results

## DISCUSSION
OPEN ISSUES
+ Showing it’s possible to get interesting services without invasive privacy practices.
+ Better handling the 10-20% of edge cases
+ Better grasping the front-back orientation of limbs due to clothing, lighting, background
+ Branching object persistence models across multiple cameras
+ Handling changing databases schema, data types and complex objects
+ Determining the metrics that improve downstream performance

## SANDBOX
+ Reliability planning: recovering gracefully from internet/power outages
+ How will the profits that accrue from increasing automation be reinvested back for collective gain?

## BIBLIOGRAPHY
+ The Great Good Place by Roy Oldenburg (1989)
+ Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)
+ @InProceedings{Li_2019_CVPR, author = {Li, Chen and Lee, Gim Hee}, title = {Generating Multiple Hypotheses for 3D Human Pose Estimation With Mixture Density Network}, booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2019} } 
+ Ye Q., Kim TK. (2018) Occlusion-Aware Hand Pose Estimation Using Hierarchical Mixture Density Network. In: Ferrari V., Hebert M., Sminchisescu C., Weiss Y. (eds) Computer Vision – ECCV 2018. ECCV 2018. Lecture Notes in Computer Science, vol 11214. Springer, Cham
+ @inproceedings{zhou2020monocular, title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data}, author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng}, booktitle={Proceedings of the IEEE International Conference on Computer Vision}, pages={0--0}, year={2020} } 
