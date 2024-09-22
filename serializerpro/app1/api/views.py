from django.shortcuts import render
from app1.api.serializers import CoderSerializer
from app1.models import Coder
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view()
def coderlist(request):
    c=Coder.objects.all()
    serializer=CoderSerializer(c,many=True)
    return Response(serializer.data)

@api_view()
def coder_data(request,pk):
    c=Coder.objects.get(pk=pk)
    serializer=CoderSerializer(c)
    return Response(serializer.data)