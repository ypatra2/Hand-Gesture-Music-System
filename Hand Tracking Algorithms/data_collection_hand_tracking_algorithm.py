import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time
import os

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 600

folder = "../Data/C2" ##change folder name based on note being stored
if not os.path.exists(folder):
    os.makedirs(folder)
counter = 0

while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame")
        success, img = cap.read()

    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255

        imgCrop = img[y - offset: y + h + offset, x - offset: x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h/w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            if imgCropShape[0] > 0 and imgCropShape[1] > 0:
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            else:
                imgResize = np.zeros((imgSize, wCal, 3), np.uint8)
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)

            imgCropResized = cv2.resize(imgCrop, (wCal, imgSize))
            imgWhite[:, wGap:wGap + wCal] = imgCropResized

        elif aspectRatio <=1:
            k = imgSize / w
            hCal = math.ceil(k * h)
            if imgCropShape[0] > 0 and imgCropShape[1] > 0:
                imgResize = cv2.resize(imgCrop, (hCal, imgSize))
            else:
                imgResize = np.zeros((imgSize, hCal, 3), np.uint8)
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)

            imgCropResized = cv2.resize(imgCrop, (hCal, imgSize))
            imgWhite[:, hGap:hGap + hCal] = imgCropResized

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f"{folder}/Image_{time.time()}.jpg",imgWhite)
        print(counter)
cap.release()
cv2.destroyAllWindows()
