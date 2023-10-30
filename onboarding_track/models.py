from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.CharField(max_length=50)
    start_date = models.DateField()
    is_onboarded = models.BooleanField(default=False)


# Create your models here.
