from django.shortcuts import render
from django.http import HttpResponse
def firstfunction(requect):
    return HttpResponse('<h1>this is my first function</h1>')
# Create your views here.
def htmlfunction(request):
    return render(request,'htmlprogrom1.html')