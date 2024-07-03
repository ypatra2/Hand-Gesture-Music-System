import queue
import threading
import time
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
from scamp import *
import time
import sys

# sys.argv[0] = "Piano"
session = Session()
piano = session.new_part(sys.argv[1])


def play_note(note):  # code to play the note
    piano.play_note(note, 1, 0.05)


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

offset = 20
imgSize = 600

folder = "../Data/C"
counter = 0

labels = ["C1", "D1", "E1", "F1", "G1", "A1", "B1", "C2"]

notes = {"C1": 60, "D1": 62, "E1": 64, "F1": 65, "G1": 67, "A1": 69, "B1": 71, "C2": 72}

note_played = "C"


def hands_detect():

    while True:
        success, img = cap.read()
        if not success:
            print("Error: Could not read frame")
            success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img)
        if hands:

            hand = hands[0]
            x, y, w, h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

            imgCrop = img[y - offset: y + h + offset, x - offset: x + w + offset]

            imgCropShape = imgCrop.shape

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                if imgCropShape[0] > 0 and imgCropShape[1] > 0:
                    img_resize = cv2.resize(imgCrop, (wCal, imgSize))
                else:
                    img_resize = np.zeros((imgSize, wCal, 3), np.uint8)
                # imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                img_resize_shape = img_resize.shape
                wGap = math.ceil((imgSize - wCal) / 2)

                img_crop_resized = cv2.resize(imgCrop, (wCal, imgSize))
                imgWhite[:, wGap:wGap + wCal] = img_crop_resized

            elif aspectRatio <= 1:
                k = imgSize / w
                hCal = math.ceil(k * h)
                if imgCropShape[0] > 0 and imgCropShape[1] > 0:
                    img_resize = cv2.resize(imgCrop, (hCal, imgSize))
                else:
                    img_resize = np.zeros((imgSize, hCal, 3), np.uint8)
                img_resize_shape = img_resize.shape
                h_gap = math.ceil((imgSize - hCal) / 2)

                img_crop_resized = cv2.resize(imgCrop, (hCal, imgSize))
                imgWhite[:, h_gap:h_gap + hCal] = img_crop_resized

            prediction, index = classifier.getPrediction(imgWhite, draw=False)


            # create a thread to play the note
            t = threading.Thread(target=play_note, args=(notes[labels[index]],))
            t.start()

            cv2.rectangle(imgOutput, (x - offset, y - offset - 50),
                          (x - offset + 90, y - offset), (255, 0, 255), cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset),
                          (x + w + offset, y + h + offset), (255, 0, 255), 4)

        cv2.imshow("Image", imgOutput)

        if cv2.waitKey(33) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


hands_thread = threading.Thread(target=hands_detect())
hands_thread.start()
