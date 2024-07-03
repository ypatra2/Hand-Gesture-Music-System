# Hand Gesture Music System
This project implements a real-time hand gesture recognition system using MediaPipe. It allows users to play music using SCAMP (Suite for Computer-Assisted Music in Python) by selecting an instrument of their choice through hand movements captured by a webcam. The instrument selection is realized through a Web App built using Streamlit in Python. This is a Human Computer Interaction (HCI) Application Project.

## Features
<li><strong>Hand Gesture Recognition: </strong>Utilizes Mediapipe for real-time hand gesture detection.</li>
<li><strong>Image Sample Generation: </strong>For each note, a unique hand gesture is made in front of the webcam, and image samples are stored as .jpg files in the corresponding Data folder. Augmented data is generated for model robustness by saving images of the gesture at different angles to the webcam.</li>
<li><strong>Model Training for Classification: </strong>Classification is required for detecting which note is being played by the user. A Deep Learning Image Classifier is trained on the sampled images stored in the Data folder, using Teachable Machine by Google (<href>https://teachablemachine.withgoogle.com/</href>).</li>
<li><strong>Sound Mapping: </strong>Each unique hand gesture is associated with a unique sound frequency, similar to how a musical keyboard is programmed</li>
<li><strong>Instrument Selection: </strong>A Streamlit Web App (<href>https://streamlit.io/</href>) is designed to allow the user to interact with this Music System. The user selects an instrument using a dropdown. The Web App displays the image of the selected instrument and plays a video generated using Synthesia.io (<href>https://www.synthesia.io/</href>) wherein an AI Avatar describes the chosen instrument.<br><br><img width="1440" alt="image" src="https://github.com/ypatra2/Hand-Gesture-Music-System/assets/86041798/49be357a-0bc9-48e5-897d-1bfc006799d2">
</li>

<li><strong>Interactive Music Playback: </strong>SCAMP (Suite for Computer-Assisted Music in Python) is used to generate the sound of the selected instrument with each unique hand gesture used to play the instrument at a different frequency.</li>

## Requirements

<li>Python 3.x</li>
<li>OpenCV</li>
<li>CVZone</li>
<li>MediaPipe</li>
<li>SCAMP</li>
<li>OpenAI</li>

## Installation
<li> Clone the repository</li>
  git clone https://github.com/Sgvkamalakar/Hand-Gesture-Music-Player.git
<li>Requirements</li>
  pip install -r requirements.txt

## Usage

<li><strong>Image Generation: </strong>Run <strong>data_collection_hand_tracking_algorithm.py </strong> and make hand gestures in front of a webcam based on the note for which the image is being saved. Remember to enter the correct save-to path in the script before running it. Use the <strong> S </strong> key to save the image displayed on the window once ready. Generate an ample number of images so that the Image Classifier has sufficient data to learn from, which will make it robust.</li>
<li><strong>Training Image Classifier: </strong> Upload images stored in the Data folder to Google Teachable Machine and enter a label for each type of gesture as per the musical note it represents. Once images are uploaded, click on Train model. After training is complete, download the <strong>.h5 file</strong> and place it in the Model folder of this repository. A trained model has already been placed in the Model folder currently. Feel free to replace it with a more extensive gesture-trained model.</li>
<li><strong>Web App Launch: </strong>Launch the Streamlit Web App using streamlit command in terminal. Make sure streamlit python library has been appropriately installed before launching the web app. Enter the folder Streamlit Web App from terminal using <strong>cd</strong> command. Then use the command <strong>streamlit run streamlit_app.py</strong> to launch the Web App in a new browser. The app is now ready to be used. Have fun!</li>

## Demo: 

[![Watch the video](https://raw.githubusercontent.com/ypatra2/Hand-Gesture-Music-System/main/Demo.mp4)]
(https://raw.githubusercontent.com/ypatra2/Hand-Gesture-Music-System/main/Demo.mp4)




