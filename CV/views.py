from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def faceapi(request):
    return render(request, 'face-api.html')