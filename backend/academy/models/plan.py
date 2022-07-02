from email import message
from statistics import mode
from django.db import models
from accounts.models.user import User


class planMessage(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sender')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class plan(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    description = models.TextField()

    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="plan_teacher")
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="plan_student")
    semesters = models.ManyToManyField(
        'semester', related_name='plan_semester')

    messages = models.ManyToManyField(planMessage, blank=True)
