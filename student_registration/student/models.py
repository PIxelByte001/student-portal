from django.db import models
from django.contrib.auth.models import User


class stu_details(models.Model):
    id = None
    email = models.OneToOneField(User, to_field='username', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    application_filled = models.BooleanField(default=False)
    status = models.IntegerField(default=0)

    REQUIRED_FIELDS=['name', 'contact']

    def __str__(self):
        return str(self.email)
