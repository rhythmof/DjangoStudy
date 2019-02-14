from django.urls import path
from shop.views import shop_list

app_name = 'shop'  # URL Reverse 기능을 할 때, 사용.

urlpatterns = [
    path('shop_list', shop_list),
]