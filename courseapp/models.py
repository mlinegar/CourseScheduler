from django.db import models
from django.contrib.postgres.fields import ArrayField

class Courses(models.Model):
    term_code = models.CharField(max_length=6)
    # build in regex?
    def year(self):
        return self.term_code[:4]
    def term(self):
        tc = self.term_code[5:]
        if tc == '01':
            tt = 'Fall'
        elif tc == '02':
            tt = 'Paideia'
        elif tc == '03':
            tt = 'Spring'
        elif tc == '04':
            tt = 'Summer'
        else:
            tt = 'Error: Invalid term'
        return tt
    CRN = models.CharField(max_length = 5)
    def Courses_pk(self):
        k = self.term_code + self.CRN
        return k
        # should I set this as pk? Do pk's have to be integers?
    note = models.CharField(max_length = 250, default='')
    course = models.CharField(max_length = 12, default='')
    title = models.CharField(max_length = 50, default='')
    xlist = ArrayField(models.CharField(max_length=12))
    instructor = models.CharField(max_length = 122, default='')
    group = ArrayField(models.CharField(max_length=1))
    graduate_level = models.BooleanField(default=False)
    year_long = models.BooleanField(default=False)
    subject = models.CharField(max_length = 30, default='')
    status = models.CharField(max_length = 9, default='')
    units = models.DecimalField(max_digits = 3, decimal_places = 1)
    add_me = models.CharField(max_length=200, default='')

class Courses_location(models.Model):
    Course = models.ForeignKey(Courses)
    day_number = models.CharField(max_length=1)
    start_date = models.DateField
    end_date = models.DateField
    SUN_day = models.BooleanField(default=False)
    MON_day = models.BooleanField(default=False)
    TUE_day = models.BooleanField(default=False)
    WED_day = models.BooleanField(default=False)
    THU_day = models.BooleanField(default=False)
    FRI_day = models.BooleanField(default=False)
    SAT_day = models.BooleanField(default=False)
    begin_time = models.CharField(max_length=5)
    end_time = models.CharField(max_length=5)
    def day(self):
        # this is certainly a bad/inefficient way to define day, but it's temporary
        d = ''
        if self.SUN_day:
            d = d + "Su"
        if self.MON_day:
            d = d + "M"
        if self.TUE_day:
            d = d+ "Tu"
        if self.WED_day:
            d = d + "W"
        if self.THU_day:
            d = d + "Th"
        if self.FRI_day:
            d = d + "F"
        if self.SAT_day:
            d = d + "Sa"
        return d
    def time(self):
        t = self.begin_time + "-" + self.end_time
        return t
    def total_time(self):
        t = self.day + " " + self.time
        return t
    building = models.CharField(max_length=6)
    room = models.CharField(max_length=12)
    def location(self):
        loc = self.building + " " + self.room
        return loc
