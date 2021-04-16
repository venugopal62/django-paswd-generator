from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def back(request):
    return render(request, 'generator/home.html')
def abovepage(request):
    return render(request, 'generator/abovepage.html')
def home(request):
    return render(request, 'generator/home.html', {'password':'django'})
def frame(request):
    return HttpResponse("<h1>this is a framework</h1>")
def password(request):
    thepassword = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))

    length = int(request.GET.get("length"))
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {"password":thepassword})
