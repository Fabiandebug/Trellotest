from unicodedata import name
from django import views
from django.db import router
from . views import userapi
from django.urls import path,include


urlpatterns=[

 path('userapi/',userapi.as_view(),name='userapiclass'),

]
