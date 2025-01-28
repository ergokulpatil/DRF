from django.contrib import admin
from django.urls import path
from app1.api.views import DoctorDetails,DoctorList, HospitalList,HospitalDetails
urlpatterns = [
    path('doctorlist/',DoctorList.as_view(), name='doctorlist' ),
    path('doctor_data/<int:pk>/',DoctorDetails.as_view(), name='doctor_data' ),
    path('hospitallist/',HospitalList.as_view(), name='hospitallist' ),
    path('hospital_data/<int:pk>/',HospitalDetails.as_view(), name='hospital_data' ),
]
