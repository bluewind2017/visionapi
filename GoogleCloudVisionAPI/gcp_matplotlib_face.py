
import os
import io
from google.cloud import vision
from matplotlib import pyplot as plt
from matplotlib import patches as pch

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="vision2020-333ceb3eedaa.json"
# os.path.join(os.curdir, 'credentials.json')

client = vision.ImageAnnotatorClient()

f = 'resources/face_no_surprise.jpg'
with io.open(f, 'rb') as image:
    content = image.read()

image = vision.Image(content=content)
response = client.face_detection(image=image)
faces = response.face_annotations

possibility = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY',
               'POSSIBLE', 'LIKELY', 'VERY_LIKELY')

a = plt.imread(f)
fig, ax = plt.subplots(1)
ax.imshow(a)

for face in faces:
    print('Possibility of anger: {}'.format(possibility[face.anger_likelihood]))
    print('Possibility of joy: {}'.format(possibility[face.joy_likelihood]))
    print('Possibility of surprise: {}'.format(possibility[face.surprise_likelihood]))
    print('Possibility of sorrow: {}'.format(possibility[face.sorrow_likelihood]))

    vertices = ([(vertex.x, vertex.y)
                 for vertex in face.bounding_poly.vertices])

    print('Vertices covering face: {}\n\n'.format(vertices))

    rect = pch.Rectangle(vertices[0], (vertices[1][0] - vertices[0][0]),
                         (vertices[2][1] - vertices[0][1]), linewidth=1,
                         edgecolor='r', facecolor='none')
    ax.add_patch(rect)

print('Confidence in Detection: {}%'.format(
    face.detection_confidence * 100))

plt.show()
