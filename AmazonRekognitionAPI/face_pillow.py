import boto3
from PIL import Image, ImageDraw

BUCKET = "<BUCKET_NAME>"
KEY = "<IMAGE_KEY>"
ACCESS_KEY = "<ACCESS_KEY>"
SECRET_KEY = "<SECRET_KEY>"
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")

def detect_faces(bucket, key, attributes=['ALL'], region="<REGION>"):
    rekognition = boto3.client("rekognition", region,
                            aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY)
    response = rekognition.detect_faces(
        Image={
            "S3Object": {
                "Bucket": BUCKET,
                "Name": KEY
            }
        },
        Attributes=attributes,
    )
    return response['FaceDetails']

detected_faces = detect_faces(BUCKET, KEY)

if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

# Image with the same name as in s3 bucket is opened locally
im = Image.open(KEY)
imgWidth, imgHeight = im.size

draw = ImageDraw.Draw(im)

# calculate and display bounding boxes for each detected face
for faceDetail in detected_faces:
    box = faceDetail['BoundingBox']
    left = imgWidth * box['Left']
    top = imgHeight * box['Top']
    width = imgWidth * box['Width']
    height = imgHeight * box['Height']

    points = (
        (left,top),
        (left + width, top),
        (left + width, top + height),
        (left , top + height),
        (left, top)

    )
    draw.line(points, fill='#00d400', width=2)

im.show()
