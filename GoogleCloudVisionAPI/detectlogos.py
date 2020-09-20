import os, io
from google.cloud import vision
from draw_vertice import drawVertices

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'vision2020-290100-c6b16014803d.json'
client = vision.ImageAnnotatorClient()

file_name = 'logos.png'
image_folder = './resources/'
image_path = os.path.join(image_folder, file_name)

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.logo_detection(image=image)
logos = response.logo_annotations

for logo in logos:
    print('Logo Description:', logo.description)
    print('Confidence Score:', logo.score)
    print('-'*50)
    vertices = logo.bounding_poly.vertices
    print('Vertices Values {0}'.format(vertices))
    drawVertices(content, vertices, logo.description)
    
    
----------draw_vertice.py-----------
import io
from PIL import Image, ImageDraw, ImageFont

def drawVertices(image_source, vertices, display_text=''):
    pillow_img = Image.open(io.BytesIO(image_source))

    draw = ImageDraw.Draw(pillow_img)
    for i in range(len(vertices) - 1):
        draw.line(((vertices[i].x, vertices[i].y), (vertices[i + 1].x, vertices[i + 1].y)),
                fill='green',
                width=8
        )

    draw.line(((vertices[len(vertices) - 1].x, vertices[len(vertices) - 1].y),
               (vertices[0].x, vertices[0].y)),
               fill='green',
               width=8
    )

    font = ImageFont.truetype('arial.ttf', 16)
    draw.text((vertices[0].x + 10, vertices[0].y),
              font=font, text=display_text,
              fill=(255, 255, 255))
    pillow_img.show()
