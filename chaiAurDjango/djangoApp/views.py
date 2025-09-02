from django.shortcuts import render
from django.http import HttpResponse
from .models import chaiVariety


def main(request):
    return render(request,'djangoApp/main.html')

def all_chai(request):
    chais = chaiVariety.objects.all
    return render(request,'djangoApp/main.html',{'chais':chais})



# Create your views here.
