from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=20,unique=True)
    course=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.roll_no}"
