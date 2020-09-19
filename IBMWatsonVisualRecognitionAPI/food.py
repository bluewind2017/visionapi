import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('0Q6XzIINBWyB4X-i6CViERgaew85Uxzio17bqbRym3f1')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.kr-seo.visual-recognition.watson.cloud.ibm.com/instances/a5282502-54eb-4b8e-aadd-1c814ac28faa')

url = 'https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/fruitbowl.jpg'
classifier_ids = ["food"]


classes_result = visual_recognition.classify(url=url, classifier_ids=classifier_ids).get_result()
print(json.dumps(classes_result, indent=2))
