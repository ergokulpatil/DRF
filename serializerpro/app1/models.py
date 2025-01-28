from django.db import models

# Create your models here.
# class Coder(models.Model):
#     first_name = models.CharField(max_length=55)
#     exp = models.IntegerField()
#     skills = models.CharField(max_length=66)


#     def __str__(self):
#         return self.first_name

class Hospital(models.Model):
    name=models.CharField(max_length=111)
    desc=models.CharField(max_length=111)
    loc=models.CharField(max_length=55)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    Dname=models.CharField(max_length=111)
    about=models.CharField(max_length=111)
    website=models.URLField(max_length=111)

    def __str__(self):
        return self.Dname
