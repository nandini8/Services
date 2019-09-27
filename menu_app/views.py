from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        return HttpResponseRedirect('command')
    return render(request, 'index.html')

def command(request):
    ## Playbook processing
    return render(request, 'demo.html')