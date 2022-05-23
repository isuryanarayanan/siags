from django.db import models
from accounts.models.user import User
from quizzes.models import quiz


class courseData(models.Model):
    """
    Course data model integrates every course display
    information into one.
    """

    # Course details
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        verbose_name = "course data"
        verbose_name_plural = "course datas"
        app_label = "course"

    def __str__(self):
        return f'{self.title} | {self.code}'


class courseAssesment(models.Model):
    """
    Course assesment is the single model which will be used
    for assessing a student and contain the information about the
    specific assesment.
    """

    # Assesment info
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="teacher_assesment")
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="student_assesment")
    quiz = models.ManyToManyField(quiz)
    #assignments = models.ManyToManyField(assignment)

    # Assesment results
    total = models.IntegerField()

    def save(self, *args, **kwargs):
        # for all quizzes sum up all the marks
        self.total = 0

        for quiz in self.quizzes.all():
            self.total += quiz.mark

        # for all assignments sum up all the marks
        for assignment in self.assignments.all():
            self.total += assignment.mark

        super(courseAssesment, self).save(*args, **kwargs)


class courseRelation(models.Model):
    """
    Course relation is the single model which will be used
    for display relations.
    """

    # Course relations
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="teacher_course")
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="student_course")
    course = models.ForeignKey(courseData, on_delete=models.CASCADE)

    # Assesments are models used to store info on an assesment,
    # of a certain subject with a student by a teacher
    assesments = models.ManyToManyField(courseAssesment)
