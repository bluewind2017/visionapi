import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('0Q6XzIINBWyB4X-i6CViERgaew85Uxzio17bqbRym3f1')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.kr-seo.visual-recognition.watson.cloud.ibm.com/instances/a5282502-54eb-4b8e-aadd-1c814ac28faa')

with open('./resources/beagle.zip', 'rb') as beagle, open(
        './resources/golden-retriever.zip', 'rb') as goldenretriever, open(
            './resources/husky.zip', 'rb') as husky, open(
                './resources/cats.zip', 'rb') as cats:
    model = visual_recognition.create_classifier(
        'dogs',
        positive_examples={'beagle': beagle, 'goldenretriever': goldenretriever, 'husky': husky},
        negative_examples=cats).get_result()
print(json.dumps(model, indent=2))
