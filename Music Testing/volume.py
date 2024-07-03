import cv2
import subprocess


def calculate_distance(focal_length, known_width, pixel_width):
    return (known_width * focal_length) / pixel_width


# Load the cascade
hand_cascade = cv2.CascadeClassifier('hand.xml')

# Open the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Set the width and height of the frame
cap.set(3, 640)
cap.set(4, 480)

# Set the known parameters for distance calculation
focal_length = 640
known_width = 18

while True:
    # Read the frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the hand in the frame
    hands = hand_cascade.detectMultiScale(gray, 1.1, 4)

    # If a hand is detected, calculate the distance and control the volume
    if len(hands) > 0:
        # Draw a rectangle around the hand
        (x, y, w, h) = hands[0]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Calculate the distance from the camera
        hand_mask = gray[y:y+h, x:x+w]
        pixel_width = hand_mask.shape[1]
        distance = calculate_distance(focal_length, known_width, pixel_width)

        # Set the volume based on the distance
        volume = int(100 - distance * 5)
        volume = max(0, volume)
        volume = min(100, volume)

        # Control the system volume
        subprocess.call(["osascript", "-e", "set Volume " + str(volume)])

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
