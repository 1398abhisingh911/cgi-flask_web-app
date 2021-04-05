from flask import Flask
from flask import render_template
from flask import request
import cv2
import boto3
from playsound import playsound
from datetime import datetime
import speech_recognition as sr
import json


app=Flask("MyWebMenu")

@app.route("/")
def main():
    data=render_template("main.html")
    return data

@app.route("/docker")
def docker():
    data=render_template("docker.html")
    return data


@app.route("/aws")
def aws():
    data=render_template("aws.html")
    return data


@app.route("/hadoop")
def hadoop():
    data=render_template("hadoop.html")
    return data

@app.route("/ansible")
def ansible():
    data=render_template("ansible.html")
    return data

@app.route("/linux")
def linux():
    data=render_template("linux.html")
    return data

@app.route("/blog")
def blog():
    data=render_template("blog.html")
    return data

@app.route("/ml")
def ml():
    data=render_template("ml.html")
    return data


@app.route('/rekognition', methods=['POST'])
def rekognition():
    
    picname= request.form.get("picname")
    upname=request.form.get("uplname")
    cap=cv2.VideoCapture(0)
    ret,pic=cap.read()
    cv2.imwrite(picname,pic)
    cap.release()
    region="ap-south-1"
    bucket="myworklw"
    s3=boto3.resource("s3")
    s3.Bucket(bucket).upload_file(picname,upname)
    rek=boto3.client('rekognition',region)
    response=rek.detect_labels(
        Image={
       
        'S3Object': {
            'Bucket': bucket,
            'Name': upname,
            
        }
    },
    MaxLabels=5,
    MinConfidence=90,
    )
    y = json.dumps(response)
    return render_template("output.html",response=y)


@app.route('/facedetection', methods=['POST'])
def facedetection():
    picname= request.form.get("picname")
    upname=request.form.get("uplname")
    cap=cv2.VideoCapture(0)
    ret,pic=cap.read()
    cv2.imwrite(picname,pic)
    cap.release()
    region="ap-south-1"
    bucket="myworklw"
    s3=boto3.resource("s3")
    s3.Bucket(bucket).upload_file(picname,upname)
    rek=boto3.client('rekognition',region)
    response=rek.detect_faces(
        Image={
       
        'S3Object': {
            'Bucket': bucket,
            'Name': upname,
            
        }
    },
    Attributes=[
        'ALL',
    ]
    )
    y = json.dumps(response)
    return render_template("output.html",response=y)


@app.route('/contentmoderation', methods=['POST'])
def contentmoderation():
    f = request.files['file']
    picname=f.filename
    upname=request.form.get("uplname")
    region="ap-south-1"
    bucket="myworklw"
    s3=boto3.resource("s3")
    s3.Bucket(bucket).upload_file(picname,upname)
    rek=boto3.client('rekognition',region)
    
    response = rek.detect_moderation_labels(
    Image={
       
        'S3Object': {
            'Bucket': bucket,
            'Name': upname
           
        }
    },
    MinConfidence=90,
    )
    y = json.dumps(response)
    return render_template("output.html",response=y)

@app.route('/polly', methods=['POST'])
def polly():
    po=boto3.client("polly")
    upname=request.form.get("speech")
    now = datetime.now()
    filename= now.strftime("%f")
    filename=filename+".mp3"
    res=po.synthesize_speech(Text=upname,OutputFormat="mp3",VoiceId='Aditi')
    file=open(filename,'wb')
    file.write(res['AudioStream'].read())
    file.close()
    playsound(filename)

    return render_template("output.html",response="Audio SAVED")


@app.route('/comprehendsyn', methods=['POST'])
def comprehend():
    client = boto3.client('comprehend')
    upname=request.form.get("speech")
    response = client.batch_detect_syntax(
    TextList=[
        upname,
    ],
    LanguageCode='en'
    )
    return render_template("output.html",response=response)


@app.route('/comprehendsen', methods=['POST'])
def comprehendsen():
    client = boto3.client('comprehend')
    upname=request.form.get("speech")
    response = client.batch_detect_sentiment(
    TextList=[
        upname,
    ],
    LanguageCode='en'
    )
    return render_template("output.html",response=response)

@app.route('/comprehendphrases', methods=['POST'])
def comprehendphrases():
    client = boto3.client('comprehend')
    upname=request.form.get("speech")
    response = client.batch_detect_key_phrases(
    TextList=[
        upname,
    ],
    LanguageCode='en'
    )
    return render_template("output.html",response=response)


@app.route('/comprehendentities', methods=['POST'])
def comprehendentities():
    client = boto3.client('comprehend')
    upname=request.form.get("speech")
    response = client.batch_detect_entities(
    TextList=[
        upname,
    ],
    LanguageCode='en'
    )
    return render_template("output.html",response=response)



@app.route('/translate', methods=['POST'])
def translate():
    client = boto3.client('translate')
    upname=request.form.get("speech")
    source=request.form.get("source")
    target=request.form.get("target")

    response = client.translate_text(
    Text=upname,
    
    SourceLanguageCode=source,
    TargetLanguageCode=target
    )
    return render_template("output.html",response=response)




if __name__ == '__main__':
        app.run(debug= True)
