from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', login_views, name='index'),
    path('admin/', admin_views, name='admin'),
    path('main/', main_views, name='main'),
    path('logout/', logout_views, name='logout'),
    path('changepwd', changepwd_view, name='changepwd')

]