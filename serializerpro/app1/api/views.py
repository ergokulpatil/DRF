from django.shortcuts import render
from app1.api.serializers import CoderSerializer
from app1.models import Coder
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.
@api_view(['GET', 'POST'])
def coderlist(request):
    if request.method=='GET':
        
        c=Coder.objects.all()
        serializer=CoderSerializer(c,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=CoderSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT','DELETE'])
def coder_data(request,pk):
    if request.method=='GET':
        try:
            c=Coder.objects.get(pk=pk)
        except Coder.DoesNotExist:
            return Response({'error':'Coder record not found'},status=status.HTTP_404_NOT_FOUND) 
               
        serializer=CoderSerializer(c)
        return Response(serializer.data)
    if request.method=='PUT':
        c=Coder.objects.get(pk=pk)
        serializer=CoderSerializer(c,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=="DELETE":

        c=Coder.objects.get(pk=pk)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
