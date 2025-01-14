import cv2
import os
import numpy as np
from PIL import Image

# Function to train face recognition model
def train_image():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces, ids = [], []
    for image_path in os.listdir('TrainingImage'):
        if image_path.endswith('.jpg'):
            img_path = os.path.join('TrainingImage', image_path)
            img = Image.open(img_path).convert('L')  # Convert to grayscale
            img_array = np.array(img, 'uint8')
            id_ = int(image_path.split('_')[0])  # Extract ID from filename
            faces.append(img_array)
            ids.append(id_)

    recognizer.train(faces, np.array(ids))
    if not os.path.exists('trainer'):
        os.makedirs('trainer')
    recognizer.save('trainer/trainer.yml')
    print("Training Complete")

# Function to recognize faces
def recognize_face():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Unable to access the camera")
        return

    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame from camera")
            break
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            id_, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if confidence < 100:  # Lower confidence is better
                name = f"ID: {id_}"
            else:
                name = "Unknown"

            cv2.putText(img, name, (x, y - 10), font, 0.8, (255, 255, 255), 2)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Face Recognition', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# To run training and recognition
train_image()
recognize_face()
