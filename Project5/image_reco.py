from picamera import PiCamera
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from tempfile import gettempdir
from contextlib import closing
import subprocess
import os
import sys


def capture_image():
    camera.capture('image.jpg')
    
def upload_to_s3(filename= None):
    s3 = boto3.client("s3")
    s3.upload_file("/home/pi/Desktop/EID/Final_Project/image.jpg", "my-wand-project", "image.jpg")
    

def detect_labels():
    reko = boto3.client('rekognition', region_name = "us-east-1")
    response = reko.detect_labels(Image={'S3Object':{'Bucket':"my-wand-project",'Name':"image.jpg"}},
        MaxLabels=10)
    for label in response['Labels']:
        print("Labels : " + label['Name'])
        print("Confidence" + str(label['Confidence']))
        if int(label['Confidence']) >= 80:
            return label['Name']
        
def text_to_speech(text):
    session = boto3.Session(region_name = "us-east-1")
    polly = session.client("polly", region_name = "us-east-1")
    try:
        response = polly.synthesize_speech(Text=text, OutputFormat="mp3",
                                        VoiceId="Joanna")
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)
    
    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")

            try:
            # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)
        

    else:
        print("Could not stream audio")
        sys.exit(-1)
    subprocess.call(['xdg-open', output])
    
    
camera = PiCamera()
capture_image()
upload_to_s3()
new_label = detect_labels()
print (new_label)
if new_label is not None:
    text_to_speech(new_label+ "zzzzzzz")
