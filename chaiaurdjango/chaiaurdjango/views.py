# this is a request handleer file
#it generates http response

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello world. This is chai aur django home page")
    return render(request,'website/index.html')
def about(request):
    #return HttpResponse("hello world. This is chai aur django about page")
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')