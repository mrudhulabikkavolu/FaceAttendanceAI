import cv2
import os
import time
import sys

if len(sys.argv) > 1:
    person_name = sys.argv[1]
else:
    person_name = input(
        "Enter Student Name: "
    ).strip()

folder_path = f"dataset/{person_name}"

os.makedirs(folder_path, exist_ok=True)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

poses = [
    "STRAIGHT",
    "LEFT",
    "RIGHT",
    "UP",
    "DOWN"
]

images_per_pose = 10

cap = cv2.VideoCapture(0)

count = 0

for pose in poses:

    print(f"\n===== LOOK {pose} =====")

    for sec in range(3, 0, -1):
        print(f"Capturing in {sec}...")
        time.sleep(1)

    pose_count = 0

    while pose_count < images_per_pose:

        success, img = cap.read()

        if not success:
            continue

        img = cv2.flip(img, 1)

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_detector.detectMultiScale(
            gray,
            1.1,
            5
        )

        for (x, y, w, h) in faces:

            cv2.rectangle(
                img,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            face = gray[
                y:y+h,
                x:x+w
            ]

            face = cv2.resize(
                face,
                (200, 200)
            )

            count += 1
            pose_count += 1

            filename = os.path.join(
                folder_path,
                f"{pose.lower()}_{pose_count}.jpg"
            )

            cv2.imwrite(
                filename,
                face
            )

            time.sleep(0.3)

            break

        cv2.putText(
            img,
            f"{pose} : {pose_count}/{images_per_pose}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "Smart Dataset Collection",
            img
        )

        cv2.waitKey(1)

print(
    f"\nDataset Collection Completed!"
)

print(
    f"Total Images Saved: {count}"
)

cap.release()
cv2.destroyAllWindows()