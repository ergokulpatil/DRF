from rest_framework import serializers
from app1.models import Coder
class CoderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=55)
    exp = serializers.IntegerField()
    skills = serializers.CharField(max_length=66)
 
    def create(self, validated_data):

        return Coder.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.exp = validated_data.get('exp', instance.exp)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.save()
        return instance