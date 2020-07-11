*** WORKING PAPER ***

*** ATTACHED CODE IS FOR A PEOPLE/FOOTFALL COUNTER (PROOF-OF-CONCEPT) *** 

# I. INTRODUCTION
+ Hi there! I've long been curious about neighborhood markets (corner stores, coffeeshops, bakeries, small pharmacies). I often ask myself, could its checkout be simpler.  My thought is yes. If you were to modify neighborhood markets to run on autonomous checkout systems staff would be free from the POS and available to:  
    + chat with customers for no specific purpose 
    + be the public characters that “keep an eye” on the neighborhood 
    + be a “port of entry" for newcomers 
    + other operational duties
+ I believe neighborhood markets are an intrinsically valuable space within cities. This research explicitly focuses on giving neighborhood markets every edge. I want to bring them the tools and services of big players, but also help them keep their atmosphere and vibe. My focus is on making it feel like a natural, simple extension of the existing shopping experience. 
+ The concept is beautifully simple: make checkout so easy it feels you're stealing. Guests walk into a market, select items, walk out and upon exit the bill is sent to them via SMS that closes them out thru a mobile payment system.  

# WHY?
+ I believe training a computer vision model requires a somewhat different set of tools than most developers are currently equipped with.  In the case of neighborhood markets, developers need a deep understanding of computer vision and the socio-cultural landscape of neighborhood markets.  Because of this dual complexity, collaborations with other disciplines needs to be the norm. If computer vision developers want to contribute to the great problems of the day, research must move in an intrinsic and interdisciplinary direction.  

# TWO RESEARCH QUESTIONS
+ Through a combination of ethnography, computer vision and off-the-shelf overhead camera our system syncs specific points and items in a room with classifications across 400+ classes. To do this our computer vision model need training data.  My research explores better ways to generate this training data.
+ The focus then becomes... **How can we translate neighborhood market ethnography into a usable coherent format for training computer vision models?**   I believe translators are only products of their time and culture, so our ethnographic field notes must reflect a deep understanding of the social, environmental and governance structures of each neighborhood market.
+ I also explore (BUT not in this research)... How can we underpin our compute vision application with a public log of all queries run on the video stream data, so "the watchers themselves are watched"?  Right now a working model has video stream data staying on the hardware/off-the-shelf camera itself. Edge-cloud software lets neighborhood market staff/mgmt perform analysis, but ONLY in-house, there is no copying or moving of data outside for processing. Even then, mgmt is not given free roam to pick and prod customer data. We provide scripts which lets mgmt tease guest records with a log of every action taken. I want to show it's possible to create interesting computer vision applications that better respect guest privacy expectations.  

# METHODS --> HUMAN ETHNOGRAPHY
+ What is ethnographic research? It is sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world. Ethnographic field notes include: sensory impressions, personal responses, insider language, questions about behaviors, neighborhood identities, jottings, etc. I undertook approximately 10 months of ethnographic data collection in two neighborhood markets.  Next, **I built clever software for translating these field notes into usable data for training computer vision models.**

# METHODS --> HUMAN-COMPUTER VISION MODEL
+ I train a computer vision model to learn from translated ethnography, bounding boxes and thousands of bits of feedback from humans to understand which choices are closest to the desired behavior.  **We want the "reward function" of our system to come from taking advice from humans in a collaborative process.** Ideally our computer vision model system will learn to gaze at the world with some human-like empathy.  The idea is still in its infancy.  There is plenty of room for improvement.

# TIMELINE
+ Winter 2018 — Spring 2020 
    + Conceptualizing, Literature Review & Ethnography
+ Summer 2020 
    + Proof-Of-Concept:  People/Footfall Counter  
    + Prototype:  Tracking Gestures & Classifying Items in Neighborhood Markets 
+ Fall 2020 
    + Prototype: "Building a Cart" w/ SMS Payment Upon Exit
    + Features: Inventory Assistant & Purchasing Assistant 

# PROOF-OF-CONCEPT 
01 Installing Required Packages and Libraries 
+ Python
+ OpenCV https://opencv.org/
+ dlib http://dlib.net/a

02 Configuring Edge Computing Device
+ Prep
+ Notes

+ Code


03 Footfall/People Counter | Counts the # of people entering and exiting a room 
+ Prep
+ Notes

+ Videos
    + .avi
    + .mp4
    + .mp4
+ Output
    + .avi
+ cognition
    + init__.py
    + centroidtracker.py
    + directioncounter.py
    + trackableobject.py
+ people_counter.py

# PROTOTYPE 
04 Installing Required Packages and Libraries 
+ scikit-image https://scikit-image.org/
+ scikit-learn https://scikit-learn.org/stable/index.html
+ Numpy https://numpy.org/install/
+ Keras https://keras.io/
+ Tensorflow https://www.tensorflow.org/
+ Caffe http://caffe.berkeleyvision.org/

**05 Translating Ethnographic Field Notes**
+ At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.

06A 2D Human Pose Estimation with Tensorflow and Caffe 
+ Who’s here? 
![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)

06B Feature Extraction 
+ Who's here?

06C 3D Human Pose Estimation 
+ Who's here?

07 Training and Deploying a Hand Motion and Object Recognition Model 
+ Whatcha up to?

08 Training and Deploying a Custom Objects Classifier
+ Whatcha holdin?

**09 Reinforcement Learning using Human Feedback**
+ Who has what? (Temporal Association, "Building a Cart")

10 Action Analysis Based on Location 
+ SMS Payment Upon Exit

# V. EXPERIMENTS AND RESULTS
+ Summary Statistics
    + Accuracy 
    + Computation Speed
    + System Requirements
    + Model Size
    + Other
+ Datasets and Protocols
+ Results

# DISCUSSION

# APPENDIX: POLICY MEMORANDUM 
+ How will the profits that accrue from increasing automation be reinvested back into communities for collective gain? 
+ In a society that respects labor rights, each person would receive a cash payment equal to their share of the value of an automation-tax, taken on industry in pursuit of economic gain.  Fee proceeds called the “universal basic dividend” would go to all in that community, to each an equal amount.  An automation-tax on robots also provides industry with an incentive to ensure sufficient re-training, especially of low skilled workers or they bear the full brunt of the automation-tax.
+ We understand some may see the automation-tax as an innovation penalty.  Some companies may move elsewhere to avoid the tax.  Others may see the labor-intensive, redundant tasks saved by automation as a way to transform the way they do  operations, and in some ways reshape what it means to be a neighborhood market.

## APPENDIX: SANDBOX
+ Show it’s possible to get interesting services without egregious and invasive privacy practices (NO FACE RECOGNITION)
+ Better handling the 10% of "edge cases" (unusual cases that are not common in training data)
+ Branching object persistence models across multiple cameras
+ Better understanding the front-back orientation of human limbs due to clothing, lighting, background
+ Lower processing power bills and bridge the Edge-Cloud barrier
+ Determine the metrics that improve downstream performance
  
## BIBLIOGRAPHY
+ The Great Good Place by Roy Oldenburg (1989)
+ Writing Ethnographic Field Notes, 2nd Edition by Emerson, Fretz and Shaw (2011)

+ @InProceedings{Li_2019_CVPR, author = {Li, Chen and Lee, Gim Hee}, title = {Generating Multiple Hypotheses for 3D Human Pose Estimation With Mixture Density Network}, booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}, month = {June}, year = {2019} } 
+ Ye Q., Kim TK. (2018) Occlusion-Aware Hand Pose Estimation Using Hierarchical Mixture Density Network. In: Ferrari V., Hebert M., Sminchisescu C., Weiss Y. (eds) Computer Vision – ECCV 2018. ECCV 2018. Lecture Notes in Computer Science, vol 11214. Springer, Cham
+ @inproceedings{zhou2020monocular, title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data}, author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng}, booktitle={Proceedings of the IEEE International Conference on Computer Vision}, pages={0--0}, year={2020} } 
+ @inproceedings{martinez_2017_3dbaseline,
  title={A simple yet effective baseline for 3d human pose estimation},
  author={Martinez, Julieta and Hossain, Rayat and Romero, Javier and Little, James J.},
  booktitle={ICCV},
  year={2017}
}
+ @misc{christiano2017deep,
    title={Deep reinforcement learning from human preferences},
    author={Paul Christiano and Jan Leike and Tom B. Brown and Miljan Martic and Shane Legg and Dario Amodei},
    year={2017},
    eprint={1706.03741},
    archivePrefix={arXiv},
    primaryClass={stat.ML}
}
