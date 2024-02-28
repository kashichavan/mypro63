from django.urls import path
from .views import *

app_name='myapp'

urlpatterns = [
    path('home/',home,name='home'),
    path('contact/',contact,name='contact'),
]
