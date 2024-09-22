from rest_framework import serializers

class CoderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=55)
    exp = serializers.IntegerField()
    skills = serializers.CharField(max_length=66)
 
