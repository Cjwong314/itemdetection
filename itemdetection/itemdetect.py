import boto3
import json
import os
import cv2
import ssl


def take_photo(pic,  port=0, ramp_frames=30, x=1280, y=720):  
    camera = cv2.VideoCapture(0)
 #Camera Resolution
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    camera.set(3, x)
    camera.set(4, y)
 # Adjust camera lighting
    for i in range(ramp_frames):
        temp = camera.read()
    retval, im = camera.read()
 #Takes Photo
    cv2.imwrite("test.jpg",im)
    print("photo" + str(pic) + "taken")

#Removes Photo
    del(camera)

def upload_photo(pic,bucket):
    s3 = boto3.resource('s3')
    #s3.meta.client.upload_file('/Users/cjwong/Desktop/solving_school_shootings/'+str(pic), 'gun-rekognition', str(pic))
    s3.meta.client.upload_file(str(pic), bucket, str(pic))
    print("photo uploaded")

def detect_labels(pic, bucket):

    session = boto3.Session()
    client = session.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':pic}},
    MaxLabels=10)

    print('Detected labels for ' + pic)
    print()
    for label in response['Labels']:
        print("Label: " + label['Name'])
        print("Confidence: " + str(label['Confidence']))
        print("Instances:")
#This is where it checks to see if there is a Aluminum in the image
        if label['Name'] == "Steel":
            print("Parents:")
            return
        elif label['Name'] == "Foil":
            print("Parents:")
            return
        elif label['Name'] == "Aluminium":
            print("Parents:")
            return
        elif label['Name'] == "Can":
            print("Parents:")
            return
            
#This is where it checks to see if there is a Glass in the image
        elif label['Name'] == "Glass":
            print("Parents:")
            return
        elif label['Name'] == "Jar":
            print("Parents:")
            return
        
#This is where it checks to see if there is a Paper in the image
        elif label['Name'] == "Paper":
            print("Parents:")
            return
        elif label['Name'] == "Newspaper":
            print("Parents:")
            return
        elif label['Name'] == "Comics":
            print("Parents:")
            return
        elif label['Name'] == "Publication":
            print("Parents:")
            return
        elif label['Name'] == "Poster":
            print("Parents:")
            return
#This is where it checks to see if there is a Plastic in the image
        elif label['Name'] == "Plastic":
            print("Parents:")
            return
        elif label['Name'] == "Jug":
            print("Parents:")
            return
        elif label['Name'] == "Water":
            correctidentify()
            print("Parents:")
            return
        elif label['Name'] == "Bottle":
            correctidentify()
            print("Parents:")
            return
        for parent in label['Parents']:
            print(" " + parent['Name'])

        print("Aliases:")
        for alias in label['Aliases']:
            print(" " + alias['Name'])

            print("Categories:")
        for category in label['Categories']:
            print(" " + category['Name'])
            print("----------")
            print()

    if "ImageProperties" in str(response):
        print("Background:")
        print(response["ImageProperties"]["Background"])
        print()
        print("Foreground:")
        print(response["ImageProperties"]["Foreground"])
        print()
        print("Quality:")
        print(response["ImageProperties"]["Quality"])
        print()

    return len(response['Labels'])


def main():
    pic = "test.jpg"
    take_photo(pic)
    bucket = 'recycledetect'
    upload_photo(pic,bucket)
    label_count = detect_labels(pic, bucket)
    print("Labels detected: " + str(label_count))


main()
