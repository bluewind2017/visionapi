(base) C:\WINDOWS\system32>cd \
(base) C:\>cd vision_project
(base) C:\vision_project>conda info -e
(base) C:\vision_project>activate GoogleVision
(GoogleVision) C:\vision_project>pip install opencv-python
(GoogleVision) C:\vision_project>pip install opencv-contrib-python


-------code -------

import io
import os
import cv2
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcpvision2020-de4e1d07a050.json"
# Instantiates a client
client = vision.ImageAnnotatorClient()

def detect_text(path):
    """Detects text in the file."""
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = ''

    for text in texts:
        string+=' ' + text.description
    return string

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    file = 'live.png'
    cv2.imwrite( file,frame)

    # print OCR text
    print(detect_text(file))

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
