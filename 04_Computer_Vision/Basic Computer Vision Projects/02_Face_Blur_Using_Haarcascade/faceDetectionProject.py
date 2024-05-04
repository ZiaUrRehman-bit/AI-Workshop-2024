import cv2
import time
from random import randrange

cTime = 0
pTime = 0

cam = cv2.VideoCapture(0)
# Load some pre trained data on face frontal from opencv (haar cascade model)
trained_face_data = cv2.CascadeClassifier('I:/My Drive/Python Projects/68. Face Blur Using Harcascade/Face Detection Using HaarCascade/haarcascade_frontalface_default.xml')


while True:
    Success, frame = cam.read()
    frame = cv2.flip(frame, 1)
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # in python RGB image is actually BGR

    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # print(bboxs)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)), (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    
    cv2.imshow("Before Blur", frame)
    # if face_coordinates:
    for (x, y, w, h) in face_coordinates:
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2) # varying the color in range 0 - 256

    # (x, y, w, h) = face_coordinates

        if x < 0: x = 0
        if y < 0: y = 0

        imgCrop = frame[y:y+h, x:x+w]
        imgBlur = cv2.blur(imgCrop, (35, 35))
        frame[y:y+h, x:x+w] = imgBlur
        # cv2.imshow(f"image croped", imgCrop)

    cv2.imshow("After Blur", frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
