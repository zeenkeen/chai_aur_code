# this is a request handleer file
#it generates http response

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello world. This is chai aur django home page")
    return render(request,'index.html')
def about(request):
    return HttpResponse("hello world. This is chai aur django about page")

def contact(request):
    return HttpResponse("hello world. This is chai aur django contact page")