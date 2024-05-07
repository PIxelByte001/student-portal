from django.db import models
from student.models import stu_details


class applicationss(models.Model):
    email = models.OneToOneField(stu_details, on_delete = models.CASCADE)
    Name = models.CharField(max_length=200)
    Mothers_Name = models.CharField(max_length=30)
    Fathers_Name = models.CharField(max_length=30)
    Address = models.TextField(max_length=200)
    Contact1 = models.PositiveBigIntegerField()
    Contact2 = models.PositiveBigIntegerField()
    Class_10 = models.FloatField()
    Class_12 = models.FloatField()
    UG_CGPA = models.FloatField()
    Course = models.CharField(max_length=100)
    Photograph = models.ImageField()
    Signature = models.ImageField()

    def __str__(self):
        return self.Name


