import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Auto-generated service credentials_api_key'')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url('Auto-generated service credentials_URL')


with open('./resources/beagle.zip', 'rb') as beagle, open(
        './resources/golden-retriever.zip', 'rb') as goldenretriever, open(
            './resources/husky.zip', 'rb') as husky, open(
                './resources/cats.zip', 'rb') as cats:
    model = visual_recognition.create_classifier(
        'dogs',
        positive_examples={'beagle': beagle, 'goldenretriever': goldenretriever, 'husky': husky},
        negative_examples=cats).get_result()
print(json.dumps(model, indent=2))
