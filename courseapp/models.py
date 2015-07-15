from django.db import models

# Create your models here.
class Courses(models.Model):
    CRN = models.CharField(max_length = 5, primary_key= True)
    term = models.CharField(max_length = 10)
    year = models.CharField(max_length=4)
    note = models.CharField(max_length = 250)
    course = models.CharField(max_length = 12)
    title = models.CharField(max_length = 50)
    xlist = models.CharField(max_length = 12)
    instructor = models.CharField(max_length = 30)
    group = models.CharField(max_length = 1)
    graduate_level = models.BooleanField(default=False)
    year_long = models.BooleanField(default=False)
    subject = models.CharField(max_length = 30)
    status = models.CharField(max_length = 9)
    units = models.DecimalField(max_digits = 3, decimal_places = 1)
