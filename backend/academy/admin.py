from django.contrib import admin
from academy.models.course import course
from academy.models.semester import semester
from academy.models.plan import plan, planMessage
admin.site.register(course)
admin.site.register(plan)
admin.site.register(semester)
admin.site.register(planMessage)
