from django.db import models
from accounts.models.user import User

# Create your models here.

# assignment model


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User, related_name='assignments_owner', on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(
        User, related_name='assignments_assigned_to')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(
        'Assignment', related_name='submissions', on_delete=models.CASCADE)
    student = models.ForeignKey(
        User, related_name='submissions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='submissions/')
    grade = models.IntegerField(default=0)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.assignment.title + ' - ' + self.student.username
