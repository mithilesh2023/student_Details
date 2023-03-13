from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    father=models.CharField(max_length=200)
    mobile=models.IntegerField()
    salary=models.IntegerField()

    def __str__(self):
        return self.first_name