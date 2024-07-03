# Music-Learning-System-with-Hand-Tracking

## 1. Objective and Vision
This project aims at creating a human-computer interface application that helps bring alive the experience of learning music in a way like never before. Learning in classrooms often brings along with it a certain amount of boredom unless there is some application that can make things exciting and rejuvenate young minds. To make this more interesting, exciting new technology with the right guided approach can make learning not only more effective but also spike a general inclination towards asking questions, and critical thinking and creativity. The idea of this project is to enable young primary school kids to learn more about different instruments through an interactive web app and make it more interesting using hand tracking so they can learn about any instrument of their choice, from a set of options, learn more about it and also have the opportunity to play that instrument simply with their hand gestures, not requiring dexterity of any kind at their tender age to enjoy the experience.

## 2. Methodology
### 2.1. Hand Tracking
Hand tracking technology is the cornerstone of this project. Hand tracking has significantly changed and enhanced user experiences across technological and industrial platforms. It has been the foundation for sign language comprehension, menu controls with hand gestures as well as all applications involved in the next most cutting-edge area of Human Computer Interaction: _Augmented Reality._

![image](https://github.com/ypatra2/Music-Learning-System-with-Hand-Tracking/assets/86041798/5cfcf7d5-00c5-494b-b429-572cc338eada)
<br> <p style="text-align:center"> Figure 1: Hand Tracking Demo </p>

Accurate measurement of hand tracking has been a difficult task in the field of computer vision. However, Google’s MediaPipe Hands is an excellent high-fidelity finger and hand tracking solution which is driven by a ML (machine learning) pipeline that infer 3 dimensional landmarks from a single captured image frame. The MediaPipe Hands ML algorithm can also extend to both hands and this technology begs for thorough research in this area with a scope of a huge variety of creative and new applications, one of which has been developed and pursued in this project. The pipeline consists of two machine learning models namely the Palm Detection Model and the Hand Landmark Model. This project uses hand gestures like hand gestures used in American Sign Language. A model was newly trained on synthesized data with the help of cv2 and cvzone python packages to create this project’s training dataset for hand sign detection.



