from django.shortcuts import render
from app1.api.serializers import DoctorSeralizer, HospitalSeralizer
from app1.models import Doctor,Hospital
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class DoctorList(APIView):
    def get(self,request):
        c=Doctor.objects.all()
        serializer=DoctorSeralizer(c, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=DoctorSeralizer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DoctorDetails(APIView):
    def get(self, request, pk):
        c=Doctor.objects.get(pk=pk)
        serializer=DoctorSeralizer(c)
        return Response(serializer.data)
    
    def put(self, request,pk):
        c=Doctor.objects.get(pk=pk)
        serializer=DoctorSeralizer(c,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        
        c=Doctor.objects.get(pk=pk)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HospitalList(APIView):
    def get(self,request):
        c=Hospital.objects.all()
        serializer=HospitalSeralizer(c, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=HospitalSeralizer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class HospitalDetails(APIView):
    def get(self, request, pk):
        c=Hospital.objects.get(pk=pk)
        serializer=HospitalSeralizer(c)
        return Response(serializer.data)
    
    def put(self, request,pk):
        c=Hospital.objects.get(pk=pk)
        serializer=HospitalSeralizer(c,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        
        c=Hospital.objects.get(pk=pk)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CoderList(APIView):
#     def get(self,request):
#         c=Coder.objects.all()
#         serializer=CoderSerializer(c, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=CoderSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class CoderDetails(APIView):
#     def get(self, request, pk):
#         c=Coder.objects.get(pk=pk)
#         serializer=CoderSerializer(c)
#         return Response(serializer.data)
    
#     def put(self, request,pk):
#         c=Coder.objects.get(pk=pk)
#         serializer=CoderSerializer(c,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self,request,pk):
        
#         c=Coder.objects.get(pk=pk)
#         c.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def coderlist(request):
#     if request.method=='GET':
        
#         c=Coder.objects.all()
#         serializer=CoderSerializer(c,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer=CoderSerializer(data=request.data)
#         print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT','DELETE'])
# def coder_data(request,pk):
#     if request.method=='GET':
#         try:
#             c=Coder.objects.get(pk=pk)
#         except Coder.DoesNotExist:
#             return Response({'error':'Coder record not found'},status=status.HTTP_404_NOT_FOUND) 
               
#         serializer=CoderSerializer(c)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         c=Coder.objects.get(pk=pk)
#         serializer=CoderSerializer(c,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     if request.method=="DELETE":

#         c=Coder.objects.get(pk=pk)
#         c.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
