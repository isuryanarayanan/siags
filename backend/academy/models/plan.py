from django.db import models
from accounts.models.user import User


class plan(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    description = models.TextField()

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    semesters = models.ManyToManyField(
        'semester', related_name='plan_semester')
