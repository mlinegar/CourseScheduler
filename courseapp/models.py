from django.db import models

# Create your models here.
class Courses(models.Model):
    CRN = models.CharField(max_length = 5, primary_key= True)
    term = models.CharField(max_length = 10, default='')
    year = models.CharField(max_length=4, default='')
    note = models.CharField(max_length = 250, default='')
    course = models.CharField(max_length = 12, default='')
    title = models.CharField(max_length = 50, default='')
    xlist = models.CharField(max_length = 12, default='')
    instructor = models.CharField(max_length = 30, default='')
    group = models.CharField(max_length = 1, default='')
    graduate_level = models.BooleanField(default=False)
    year_long = models.BooleanField(default=False)
    subject = models.CharField(max_length = 30, default='')
    status = models.CharField(max_length = 9, default='')
    units = models.DecimalField(max_digits = 3, decimal_places = 1)
    days = models.CharField(max_length=5, default='')
    time = models.CharField(max_length=11, default='')
    location = models.CharField(max_length=15, default='')
    add_me = models.CharField(max_length=100, default='')