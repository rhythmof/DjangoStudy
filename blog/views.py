from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

def year_conv(request, year):
    # f: python 3.7부터 생긴 기능  (기존 format함수대체)
    return HttpResponse(f'''
        {year}에 대한 목록
    ''')

def hello(request, times): # 키워드 인자 방식이므로 이름을 정확하게!
    message = "hi" * times
    return HttpResponse(message)

def index(request):
    return render(request, 'blog/index.html')

def naver_real_keyword(request):
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')
    text = '<br/>\n'.join([tag.text for tab in tab_list])
    return HttpREsponse(text)