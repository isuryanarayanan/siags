from django.db import models


class course(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    description = models.TextField()

    elective = models.BooleanField(default=False)
    credits = models.IntegerField(default=0)
    prerequisite = models.ManyToManyField('course', blank=True)
