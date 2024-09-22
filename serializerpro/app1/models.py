from django.db import models

# Create your models here.
class Coder(models.Model):
    first_name = models.CharField(max_length=55)
    exp = models.IntegerField()
    skills = models.CharField(max_length=66)


    def __str__(self):
        return self.first_name