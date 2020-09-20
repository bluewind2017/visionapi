import os
import io
from google.cloud import vision
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'vision2020-290100-c6b16014803d.json'
client = vision.ImageAnnotatorClient()

def detect_landmark(file_path):
    try:
        with io.open(file_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)
        response = client.landmark_detection(image=image)
        landmarks = response.landmark_annotations

        df = pd.DataFrame(columns=['description', 'locations', 'score'])

        for landmark in landmarks:
            df = df.append(
                dict(
                    description=landmark.description,
                    locations=landmark.locations,
                    score=landmark.score
                ),
                ignore_index=True
            )
        return df
    except Exception as e:
        print(e)


file_name = 'landmark.jpg'
image_path = f'./resources/{file_name}'
print(detect_landmark(image_path))
