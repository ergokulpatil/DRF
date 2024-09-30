from rest_framework import serializers
from app1.models import Coder
class CoderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=55)
    exp = serializers.IntegerField()
    skills = serializers.CharField(max_length=66)
 
    def create(self, validated_data):

        return Coder.objects.create(**validated_data)
