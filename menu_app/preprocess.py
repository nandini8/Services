from .functions import *

def command_preprocessing(command):
    if command == None:
         choice = ' '
    else:
        choice = command.lower()
    print(command)

    if 'service' in choice and ('start' in choice or 'stop' in choice):
        print(choice)
        output = start_a_service()
        
    elif 'send mail' in choice:
        print(choice)
        output = send_mail()

    elif 'hadoop cluster' in choice:
        print(choice)
        output = hadoop()

    elif 'shell in a box' in choice:
        print(choice)
        output = shellinabox()
        
    elif 'docker' in choice:
        print(choice)
        output = docker_image()
        
    elif 'launch firefox' in choice:
        print(choice)
        output = firefox()
        
    elif 'elastic container' in choice:
        print(choice)
        output = ec2()

    elif 'storage' in choice and 'bucket' in choice:
        print(choice)
        output = s3()

    elif 'disk' in choice and 'partition' in choice: 
        print(choice)

    elif 'lvm' in choice and 'create' in choice:
        print(choice)
    return output