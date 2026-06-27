import cv2
import os

dataset_path = "dataset"

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

for person in os.listdir(dataset_path):

    person_folder = os.path.join(
        dataset_path,
        person
    )

    if not os.path.isdir(person_folder):
        continue

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

        faces = face_detector.detectMultiScale(
            gray,
            1.1,
            5
        )

        if len(faces) > 0:

            x, y, w, h = faces[0]

            face = gray[
                y:y+h,
                x:x+w
            ]

            face = cv2.resize(
                face,
                (200, 200)
            )

            cv2.imwrite(
                img_path,
                face
            )

            print(
                f"Processed: {img_path}"
            )

print("Dataset Preparation Complete")