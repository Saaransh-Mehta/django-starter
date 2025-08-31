from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello world. You are at chai aur django home page")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("Hello world. You are at chai aur django about page")
    return render(request,'about.html')

def comments(request):
    return HttpResponse("Hello world. You are at chai aur django comments page")

