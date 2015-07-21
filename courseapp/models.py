from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Courses(models.Model):
    term = models.CharField(max_length = 10, default='')
    CRN = models.CharField(max_length = 5, primary_key= True)
    year = models.CharField(max_length=4, default='')
    note = models.CharField(max_length = 250, default='')
    course = models.CharField(max_length = 12, default='')
    title = models.CharField(max_length = 50, default='')
    xlist = ArrayField(models.CharField(max_length=12))
    instructor = models.CharField(max_length = 30, default='')
    group = ArrayField(models.CharField(max_length=1))
    graduate_level = models.BooleanField(default=False)
    year_long = models.BooleanField(default=False)
    subject = models.CharField(max_length = 30, default='')
    status = models.CharField(max_length = 9, default='')
    units = models.DecimalField(max_digits = 3, decimal_places = 1)
    days = ArrayField(models.CharField(max_length=12))
    time = ArrayField(models.CharField(max_length=12))
    location = ArrayField(models.CharField(max_length=12))
    add_me = models.CharField(max_length=100, default='')