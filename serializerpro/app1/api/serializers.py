from rest_framework import serializers
from app1.models import Hospital,Doctor

class DoctorSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"

class HospitalSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields="__all__"

# class CoderSerializer(serializers.ModelSerializer):
#     len_names=serializers.SerializerMethodField()

#     class Meta:
#         model=Coder
#         fields="__all__"
#         #fields=['id','skills','exp']
#         #exclude=['skills']
    
#     def get_len_names(self,object):
#         l=len(object.first_name)
#         return l

# # def name_length(value):
        
# #         if len(value)<2:
# #             raise serializers.ValidationError("Name is too short")
# #         else:
# #             return value

# # class CoderSerializer(serializers.Serializer):
# #     id = serializers.IntegerField(read_only=True)
# #     first_name = serializers.CharField(max_length=55)
# #     exp = serializers.IntegerField()
# #     skills = serializers.CharField(max_length=66)
    
# #     # def validate_first_name(self,value):
# #     #     if len(value)<2:
# #     #         raise serializers.ValidationError("Name is too short")
# #     #     else:
# #     #         return value
# #     # def validate(self,data):
# #     #     if data['first_name']==data['skills']:
# #     #         raise serializers.ValidationError("name and skills should not be same")
# #     #     else:
# #     #         return data
# #     first_name=serializers.CharField(validators=[name_length])


# #     def create(self, validated_data):

# #         return Coder.objects.create(**validated_data)

# #     def update(self, instance, validated_data):
# #         instance.first_name = validated_data.get('first_name', instance.first_name)
# #         instance.exp = validated_data.get('exp', instance.exp)
# #         instance.skills = validated_data.get('skills', instance.skills)
# #         instance.save()
# #         return instance

