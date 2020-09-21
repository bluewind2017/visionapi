# (base) C:\WINDOWS\system32>cd \
# (base) C:\>cd vision_project
# (base) C:\vision_project>conda info -e
# (base) C:\vision_project>activate AmazonRekognition
# (AmazonRekognition) C:\vision_project>pip install opencv-python

import cv2
import boto3

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
while(True):
   ret, frame = cap.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   for (x,y,w,h) in faces:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
   cv2.imshow('B&W',gray)
   cv2.imshow('Color',frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break


# rekog = boto3.client('rekognition',
#                         region_name='xxxxxx-central-1',
#                         aws_access_key_id='BlaBla',
#                         aws_secret_access_key='BlaBlaXYZ'
#                   )

rekog = boto3.client('rekognition')


def send_to_rekognition(img, boto_client):
    cv2.imwrite('c:/temp/face_recog.jpg', img)
    with open("c:/temp/face_recog.jpg", "rb") as imageFile:
        f = imageFile.read()
        buf = bytearray(f)
    response = boto_client.detect_faces(
        Image={
            'Bytes': buf
        },
        Attributes=['ALL']
    )
    data = response["FaceDetails"]
    for d in data:
        print(d['Gender'])
        for e in d['Emotions']:
            print(e)


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
# Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        if cv2.waitKey(1) & 0xFF == ord('a'):
            send_to_rekognition(frame,rekog)
    # Display the resulting frame
    cv2.imshow('B&W',gray)
    cv2.imshow('Color',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



-- a :저장
-- q: 종료
