from django.contrib import admin
from django.urls import path
from django.urls import register_converter

from blog.views import hello, index
from blog.views import year_conv
from blog.views import naver_real_keyword
from blog.convert import YearConvertDo

app_name = 'blog'  # URL Reverse 기능을 할 때, 사용.
register_converter(YearConvertDo,'year')

urlpatterns = [
    path('articles/<year:year>', year_conv),
    path('hello/<int:times>/', hello), # path converter
    path('', index), # = re_path(r'^$')
    path('naver/real_time', naver_real_keyword)
]