import boto3
import json

def detect_faces(photo, bucket):
    client=boto3.client('rekognition')
    response =  client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])
    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))
    return len(response['FaceDetails'])

def main():
    photo='drive.jpg'
    bucket='visionXXXXXXX'
    face_count=detect_faces(photo, bucket)
    print("Faces detected: " + str(face_count))

if __name__ == "__main__":
    main()
