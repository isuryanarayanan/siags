from django.db import models


class semester(models.Model):
    sem = models.IntegerField(default=1)
    courses = models.ManyToManyField('course', related_name='semester_course')
    electives = models.ManyToManyField(
        'course', related_name='semester_elective', blank=True)
