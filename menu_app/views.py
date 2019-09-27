from django.shortcuts import render

from .preprocess import command_preprocessing
# Create your views here.

def run_command(command):
    output = command_preprocessing(command)
    return output


def home(request):
    if request.method == 'POST':
        command = request.POST['command']
        output = run_command(command)
        return render(request, 'demo.html', {'data': command, 'output': output})
    return render(request, 'index.html')

# def command(request):
    ## Playbook processing
    