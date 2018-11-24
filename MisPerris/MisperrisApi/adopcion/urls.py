from django.conf.urls import url
from adopcion.views import *
from django.urls import path

urlpatterns = [
    path('dogs/', DogList.as_view(), name='doglist'),  
]    
