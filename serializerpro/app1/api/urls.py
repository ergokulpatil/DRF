from django.contrib import admin
from django.urls import path
from app1.api.views import CoderList,CoderDetails
urlpatterns = [
    path('coderlist/',CoderList.as_view(), name='coderlist' ),
    path('coder_data/<int:pk>/',CoderDetails.as_view(), name='coder_data' ),
  
]
