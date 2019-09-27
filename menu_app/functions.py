'''
    Start an http server
    Start a docker image
    Shell in a box
    SaaS (firefox)
    Start an EC2 instance
    Create an S3 bucket
    Create a hadoop cluster
'''

from .playbooks import *

def start_a_service():
    return("Service Started")

def docker_image():
    return("Docker image Launched")

def shellinabox():
    return("Opened Shell in a box")

def firefox():
    return("Opened firefox")

def ec2():
    return("Created an ec2 instance")

def s3():
    return("Created an S3 bucket")

def hadoop():
    return("Created a hadoop cluster")

def send_mail():
    return("sent mail")