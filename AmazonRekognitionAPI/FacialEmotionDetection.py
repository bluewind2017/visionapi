--step#1

import boto3

#rekognition = boto3.client('rekognition',aws_access_key_id=AWS_ACCESS_KEY,  aws_secret_access_key=AWS_SECRET_KEY, region_name=AWS_REGION)

rekognition=boto3.client('rekognition')

with open('cyber.jpg', 'rb') as image_data:
    response_content = image_data.read()
rekognition_response = rekognition.detect_faces(Image={'Bytes': response_content}, Attributes=['ALL'])

print("Faces detected: " + str(rekognition_response))

# s3 에 저장된 경우
#rekognition_response = rekognition.detect_faces(Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': file_key}}, Attributes=['ALL'])


--step#2

# pip install Pillow

from PIL import Image

image = Image.open('cyber.jpg')
image_width, image_height = image.size


i = 1
for item in rekognition_response.get('FaceDetails'):
    bounding_box = item['BoundingBox']
    print('Bounding box {}'.format(bounding_box))
    width = image_width * bounding_box['Width']
    height = image_height * bounding_box['Height']
    left = image_width * bounding_box['Left']
    top = image_height * bounding_box['Top']

    left = int(left)
    top = int(top)
    width = int(width) + left
    height = int(height) + top

    box = (left, top, width, height)
    box_string = (str(left), str(top), str(width), str(height))
    print(box)
    cropped_image = image.crop(box)
    thumbnail_name = '{}.png'.format(i)
    i += 1
    cropped_image.save(thumbnail_name, 'PNG')


#step3 -Emotion Detection

i = 1
for item in rekognition_response.get('FaceDetails'):
    bounding_box = item['BoundingBox']
    print('Bounding box {}'.format(bounding_box))
    width = image_width * bounding_box['Width']
    height = image_height * bounding_box['Height']
    left = image_width * bounding_box['Left']
    top = image_height * bounding_box['Top']

    left = int(left)
    top = int(top)
    width = int(width) + left
    height = int(height) + top

    box = (left, top, width, height)
    box_string = (str(left), str(top), str(width), str(height))
    print(box)
    cropped_image = image.crop(box)
    thumbnail_name = '{}.png'.format(i)
    i += 1
    cropped_image.save(thumbnail_name, 'PNG')

    face_emotion_confidence = 0
    face_emotion = None
    for emotion in item.get('Emotions'):
        if emotion.get('Confidence') >= face_emotion_confidence:
            face_emotion_confidence = emotion['Confidence']
            face_emotion = emotion.get('Type')
    print('{} - {}'.format(thumbnail_name, face_emotion))
