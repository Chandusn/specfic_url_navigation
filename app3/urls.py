from app3.views import *
from django.urls import path

app_name='app3'

urlpatterns=[
    path('third/',third,name='third'),
]