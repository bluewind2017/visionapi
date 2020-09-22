import boto3
import json

def recognize_celebrities(photo):
    client=boto3.client('rekognition')
    
with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})

 print('Detected faces for ' + photo)      
 for celebrity in response['CelebrityFaces']:
        print ('Name: ' + celebrity['Name'])
        print ('Id: ' + celebrity['Id'])
        print ('Position:')
        print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
        print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
        print ('Info')
        for url in celebrity['Urls']:
            print ('   ' + url)
        print
    return len(response['CelebrityFaces'])

def main():
    photo='moviestars.jpg'
    celeb_count=recognize_celebrities(photo)
    print("Celebrities detected: " + str(celeb_count))

if __name__ == "__main__":
    main()
