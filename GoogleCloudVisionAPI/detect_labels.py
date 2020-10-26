-- setting 에서 panads 모듈 추가

import os
import io
from google.cloud import vision
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'vision2020-290100-c6b16014803d.json'

client = vision.ImageAnnotatorClient()

file_name = 'setagaya_small.jpeg'
image_path = f'./resources/{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# construct an iamge instance
#image = vision.types.Image(content=content)  #pip install google-cloud-vision == 1.0.0
image = vision.Image(content=content)  
response = client.label_detection(image=image)
labels = response.label_annotations

df = pd.DataFrame(columns=['description', 'score', 'topicality'])

for label in labels:
    df = df.append(
        dict(
            description=label.description,
            score=label.score,
            topicality=label.topicality
        ), ignore_index=True)

print(df)
