import datetime
import requests
import os, sys

import cv2  # opencv

if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment  variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

# Add your Computer Vision endpoint to your environment variables.
if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']
else:
    print("\nSet the COMPUTER_VISION_ENDPOINT environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

#subscription_key =  # your subscription key here

vision_analyze_url = endpoint + "vision/v3.0/analyze"


def get_image_caption(image):
    img = cv2.imencode('.jpg', image)[1].tostring()
    # Request headers
    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}
    # Request params
    params = {'visualFeatures': 'Categories,Description,Color'}
    # Make a request to the Azure Cognitive Services Vision Analysis API
    response = requests.post(vision_analyze_url, params=params,  headers=headers, data=img)
    # Extract the json from the response
    analysis = response.json()
    # Extract the captions from the output json.
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Caption with current time
    return (time_now + ": " + image_caption)


stream = cv2.VideoCapture(0)
key = None
count = 0
overlay_text = ""

while True:
    if count % 3 != 0:
        # Read frames from live web cam stream
        (grabbed, frame) = stream.read()

        # Make copies of the frame for transparency processing
        output = frame.copy()

        # Get caption to overlay
        if count % 50 == 0:
            overlay_text = get_image_caption(output)

        # Overlay caption on image
        cv2.putText(output, overlay_text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        # Show the frame
        cv2.imshow("Image", output)
        key = cv2.waitKey(1) & 0xFF

    count += 1
    # Press q to break out of the loop
    if key == ord("q"):
        break

# cleanup
stream.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
