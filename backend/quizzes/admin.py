from django.contrib import admin
from .models import quiz, question, answer, reply

# Register your models here.

admin.site.register(quiz)
admin.site.register(question)
admin.site.register(answer)
admin.site.register(reply)
