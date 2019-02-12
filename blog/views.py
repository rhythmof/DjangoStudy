from django.shortcuts import render
from django.http import HttpResponse

def hello (request, times):
    message = "hi" * times
    return HttpResponse(message)

def index(request):
    return render(request, 'blog/index.html')