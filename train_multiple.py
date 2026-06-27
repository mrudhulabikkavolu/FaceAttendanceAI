import cv2
import os
import numpy as np

dataset_path = "dataset"

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

faces = []
labels = []

label_map = {}

current_label = 1

for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(
        dataset_path,
        person_name
    )

    if not os.path.isdir(person_folder):
        continue

    label_map[current_label] = person_name

    print(f"\nProcessing {person_name}")

    for file in os.listdir(person_folder):

        img_path = os.path.join(
            person_folder,
            file
        )

        img = cv2.imread(img_path)

        if img is None:
            continue

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        detected_faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        if len(detected_faces) == 0:

            print(
                f"Skipped: {file}"
            )

            continue

        x, y, w, h = detected_faces[0]

        face = gray[
            y:y+h,
            x:x+w
        ]

        face = cv2.resize(
            face,
            (200, 200)
        )

        faces.append(face)

        labels.append(
            current_label
        )

        print(
            f"Used: {file}"
        )

    current_label += 1

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(
    faces,
    np.array(labels)
)

recognizer.save(
    "trainer.yml"
)

print("\nTraining Completed!")
print(label_map)