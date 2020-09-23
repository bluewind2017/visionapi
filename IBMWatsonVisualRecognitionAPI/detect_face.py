''' pip install --upgrade waston-developer-cloud'''

import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
	'2018-03-19',                       #  해당날짜 또는 그 날짜 이전 API버전 선택
	url='https://gateway.watsonplatform.net/visual-recognition/api',
	iam_api_key='71JiE7SU6v-gHpJPuJs6RZyoS7Py3z4Buc9zREy-pLtr')  #낮은 버전:api_key


with open('./moviestars.jpg', 'rb') as images_file:
    faces = visual_recognition.detect_faces(images_file)

print(json.dumps(faces, indent=2))
