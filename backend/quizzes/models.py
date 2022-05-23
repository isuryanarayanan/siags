from django.db import models


class quiz(models.Model):
    """
    Quiz model is the serialization layer model for the quiz app
    """

    # Quiz details
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()

    total_mark = models.IntegerField()

    class Meta:
        verbose_name = "quiz"
        verbose_name_plural = "quizzes"
        app_label = "quizzes"

    def __str__(self):
        return f'{self.title} | {self.code}'


class question(models.Model):
    quiz = models.ForeignKey(
        quiz, on_delete=models.CASCADE, related_name='question_quiz')
    text = models.CharField('Question', max_length=255)
    time = models.IntegerField(default=30)

    def __str__(self):
        return self.text


class answer(models.Model):
    question = models.ForeignKey(
        question, on_delete=models.CASCADE, related_name='answer_question')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class reply(models.Model):

    question = models.ForeignKey(
        question, on_delete=models.CASCADE, related_name='reply_question')
    quiz = models.ForeignKey(
        quiz, on_delete=models.CASCADE, related_name='reply_quiz')

    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)
    points = models.IntegerField(default=0)

    # on save
    def save(self, *args, **kwargs):

        # get all answers
        answers = answer.objects.filter(question=self.question)

        # if correct answer is the same as text set is_correct to true
        for answer in answers:
            if answer.text == self.text:
                self.is_correct = True
                self.points = self.points + self.question.total_mark
            else:
                self.is_correct = False

        super(reply, self).save(*args, **kwargs)

    def __str__(self):
        return self.text
