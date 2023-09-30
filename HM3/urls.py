from django.urls import path
from .views import index
from .views import basket, sorted_basket



urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('customer/<int:customer_id>/', basket, name='basket'),
    path('customer_sorted/<int:customer_id>/<int:days_ago>/', sorted_basket, name='sorted_basket'),


]