from django.contrib import admin
from django.urls import path
from app1.api.views import coderlist,coder_data
urlpatterns = [
    path('coderlist/',coderlist, name='coderlist' ),
    path('coder_data/<int:pk>/',coder_data, name='coder_data' ),
  
]
