from django.shortcuts import render
from django.http import HttpResponse

def year_conv(request, year):
    # f: python 3.7부터 생긴 기능  (기존 format함수대체)
    return HttpResponse(f''' 
        {year}에 대한 목록
    ''')

def hello(request, times):
    message = "hi" * times
    return HttpResponse(message)

def index(request):
    return render(request, 'blog/index.html')