import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Auto-generated service credentials_api_key'')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url('Auto-generated service credentials_URL')

url = 'https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/fruitbowl.jpg'
classifier_ids = ["food"]


classes_result = visual_recognition.classify(url=url, classifier_ids=classifier_ids).get_result()
print(json.dumps(classes_result, indent=2))
