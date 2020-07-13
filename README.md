*** WORKING PAPER ***

*** ATTACHED CODE FOR PROOF-OF-CONCEPT (PEOPLE/FOOTFALL COUNTER) ***  

# INTRODUCTION
+ Through a casual reading of weekly newspapers I noticed an increasing attention placed on community. Things are moving in this direction. It has forced businesses to do things differently to better meet community needs. Many businesses are experimenting with ways to remove once manual-processes. My research tries to remove the manual-process of ringing goods up at the neighborhood market. Personally I'd love to see neighborhood market mgmt/staff free from the point-of-sale and available to:
    + be the public characters that “keep an eye” on the neighborhood 
    + chat with guests for no specific purpose 
    + be a “port of entry" for newcomers
    + perform daily operations
+ Neighborhood markets are an intrinsically valuable space within communities. This research focuses on giving them every edge. I want to bring them the tools and services of the world's top retailers, but also help them keep their neighborhood atmosphere and vibe. My goal is to make autonomous checkout feel like a natural, simple extension of the existing shopping experience. Guests will walk into a market, select items, walk out and upon exit their bill is sent to them via SMS mobile payment. It's so easy, it almost feels like stealing!

# WHY THIS PROJECT?
+ Humans learned flight when it stopped mimicking the bird and started studying lift. It was only when humans stopped seeing flight as a symbol did human intelligence flow. Meaning and knowledge don't arise from symbols, they come from directly from our visceral needs to survive. Like many, I want to build human intelligence of survival into computers. Many would call this AI.  But what we call AI is just pattern matching. Extremely clever and powerful, but nonetheless pattern matching. Until we successfully bake this visceral human intelligence into computer vision models autonomous checkout systems won't progress beyond pattern matching.

# TIMELINE
+ Winter 2018 — Spring 2020 
    + Conceptualizing, Literature Review & Ethnography
+ Summer 2020 
    + Proof-Of-Concept:  People/Footfall Counter 
    + Alpha:  Tracking Gestures & Classifying Items in Neighborhood Markets
+ Fall 2020
    + Beta: Tracking Inventory Levels in Neighborhood Markets

# RESEARCH QUESTIONS 
+ Teach a computer vision model to use information to further its visceral motives of survival
+ Underpin a computer vision application with a public log of all queries run on its video stream data ("thus the watchers themselves are watched") 

# ETHNOGRAPHY
+ What is ethnographic research? It's a sociological method of firsthand participant observation in once unfamiliar social circles to pull a sense of what's relevant in that world.  Methods include taking field notes such as: sensory impressions, personal responses, insider language, questions about behaviors, neighborhood identities, jottings, etc. I undertook approximately 10 months of ethnographic field notes in two neighborhood markets in Chicago, IL.  I then built software for translating ethnographic field notes into usable data for training computer vision models.

# COMPUTER VISION MODEL
+  Through a combination of interdisciplinary methods, computer vision and off-the-shelf overhead cameras our system syncs specific points and items in a room with classifications across 400+ classes.  Feedback from humans fine-tune its "reward function" to relate directly to its visceral motives of survival.  Ideally our computer vision model system will learn to gaze at the world with some human-like intelligence when presented with new information to further its survival. It's only then, may its intelligence flow.

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

# ALPHA & BETA 
04 Installing Required Packages and Libraries 
+ scikit-image https://scikit-image.org/
+ scikit-learn https://scikit-learn.org/stable/index.html
+ Numpy https://numpy.org/install/
+ Keras https://keras.io/
+ Tensorflow https://www.tensorflow.org/
+ Caffe http://caffe.berkeleyvision.org/

**05 Translating Ethnographic Field Notes**
+ At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.

06a 2D Human Pose Estimation with Tensorflow and Caffe 
+ Who’s here? 
![1-DsOBzKpVMUULGABMVFdVIg](https://user-images.githubusercontent.com/40745550/82762582-6febd280-9dc7-11ea-90ea-0671e1bf3744.jpeg)

06b Feature Extraction 
+ Who's here?

06c 3D Human Pose Estimation 
+ Who's here?

07 Training and Deploying a Hand Motion and Object Recognition Model 
+ Whatcha up to?

08 Training and Deploying a Custom Objects Classifier
+ Whatcha holding?

09 Temporal Assoication 
+ Who has what? (Building a Cart from Store Shelves, Tracking Inventory Levels)

10 Action Analysis Based on Location 
+ SMS mobile payment

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
+ In a society that respects labor rights, each person would receive a cash payment equal to their share of the value of an automation-tax, taken on industry in pursuit of economic gain.  Fee proceeds called the “universal basic dividend” would go to all in that community, to each an equal amount.  An automation-tax on such systems also provides industry with an incentive to ensure sufficient re-training, especially of low skilled workers or they bear the full brunt of the automation-tax.
+ This is a policy memorandum in progress.  This means focusing a wide-angled automation-lens on regulation, rules, accounting standards, disclosure standards, stewardship codes and new intrepretations of laws must be done in partnership with market participants. 

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

+ @inproceedings{martinez_2017_3dbaseline,
  title={A simple yet effective baseline for 3d human pose estimation},
  author={Martinez, Julieta and Hossain, Rayat and Romero, Javier and Little, James J.},
  booktitle={ICCV},
  year={2017}
}
+ @inproceedings{zhou2020monocular,
  title={Monocular Real-time Hand Shape and Motion Capture using Multi-modal Data},
  author={Zhou, Yuxiao and Habermann, Marc and Xu, Weipeng and Habibie, Ikhsanul and Theobalt, Christian and Xu, Feng},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  pages={0--0},
  year={2020}
}
+ @misc{christiano2017deep,
    title={Deep reinforcement learning from human preferences},
    author={Paul Christiano and Jan Leike and Tom B. Brown and Miljan Martic and Shane Legg and Dario Amodei},
    year={2017},
    eprint={1706.03741},
    archivePrefix={arXiv},
    primaryClass={stat.ML}
}
+ @article{DBLP:journals/corr/abs-1710-09829,
  author    = {Sara Sabour and
               Nicholas Frosst and
               Geoffrey E. Hinton},
  title     = {Dynamic Routing Between Capsules},
  journal   = {CoRR},
  volume    = {abs/1710.09829},
  year      = {2017},
  url       = {http://arxiv.org/abs/1710.09829},
  archivePrefix = {arXiv},
  eprint    = {1710.09829},
  timestamp = {Mon, 13 Aug 2018 16:47:11 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1710-09829.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
