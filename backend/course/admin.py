from django.contrib import admin
from .models import courseData, courseAssesment, courseRelation

# Register your models here.

admin.site.register(courseData)
admin.site.register(courseAssesment)
admin.site.register(courseRelation)
