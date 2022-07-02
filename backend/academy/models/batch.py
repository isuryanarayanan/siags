from django.db import models
from accounts.models import User


class batch(models.Model):
    batch_id = models.CharField(max_length=10)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="teacher")
    students = models.ManyToManyField(
        User, blank=True, related_name="students")
