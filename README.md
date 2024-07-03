# Hand Gesture Music System
This project implements a real-time hand gesture recognition system using MediaPipe. It allows users to play music using SCAMP (Suite for Computer-Assisted Music in Python) by selecting an instrument of their choice through hand movements captured by a webcam. The instrument selection is realized through a Web App built using Streamlit in Python. This is a Human Computer Interaction (HCI) Application Project.

## Features
<li><strong>Hand Gesture Recognition: </strong>Utilizes Mediapipe for real-time hand gesture detectio.n</li>
<li><strong>Image Sample Generation: </strong>For each note, a specific unique hand gesture is made in front of the webcam, and image samples are stored as .jpg files in corresponding Data Folder for the note. Augmented data is generated for model robustness by saving images of the gesture at different angles to the webcam. This  using a Python script.</li>
<li><strong>Model Training for Classification: </strong>Classification is required for detecting which note is being played by the user. A Deep Learning Image Classifier is trained on the sampled images store in Data folder, using Teachable Machine by Google (<href>https://teachablemachine.withgoogle.com/</href>).</li>









