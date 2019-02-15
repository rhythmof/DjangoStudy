from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

def root(request):
    return HttpResponseRedirect('/blog/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # path converter
    path('shop/', include('shop.urls')),
    path('', root),
]