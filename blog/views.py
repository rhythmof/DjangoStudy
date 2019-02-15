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
    return render(request, 'blog/index.html') # render 함수가 response를 생성해서 준다
    # 함수에의한 view, class에 의한 view, library에 의한 view로 모두 구현 가능

def naver_real_keyword(request):
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')
    text = '<br/>\n'.join([tag.text for tag in tag_list])

    return HttpResponse(text)

def naver_blog_search(request):
    # query = request.GET.get('query') # get함수를 쓰면 key가 없으면 none을 Return
    # query = requests.GET('query') # 그냥 이렇게만 쓰면 key가 없을 때 에러남
    query = request.GET.get('query', '')
    post_list = []

    msg = f'{query} 검색할거야'

    if query:
        url = 'https://search.naver.com/search.naver'
        params = {
            'where' : 'post',
            'sm' : 'tab_jum',
            'query' : query,
        }

        res = requests.get(url, params=params)
        html = res.text
        soup= BeautifulSoup(html, 'html.parser')
        tag_list = soup.select('.sh_blog_title')

        for tag in tag_list:
            post_url = tag['href']
            post_title = tag['title']
            post_list.append('{}:{}'.format(post_url, post_title))

        # return HttpResponse(post_list)
    #     return render(request, 'blog/naver_blog_search.html', {
    #         'query' : query,
    #         'post_list' : post_list},)
    # else :
    #     msg = f'{query} 검색할거야'

    # return HttpResponse(msg)
    return render(request, 'blog/naver_blog_search.html', {
        'query' : query,
        'post_list' : post_list},)