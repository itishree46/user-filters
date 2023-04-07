from django.shortcuts import render

# Create your views here.

def filter(request):
    d={'data':'hello how are you!!'}
    return render (request,'filter.html',d)