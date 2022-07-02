from django.urls import path
from academy.api.get_batch import GetBatch
from academy.api.get_courses import GetCourses
from academy.api.send_message import sendMessage
from academy.api.get_courseplan import GetCoursePlan
from academy.api.post_courseplan import PostCoursePlan
from academy.api.create_semester import CreateSemester
from academy.api.create_courseplan import CreateCoursePlan


urlpatterns = [
    path('v1/get_batch/', GetBatch.as_view(), name='GetBatch'),
    path('v1/send_message/', sendMessage.as_view(), name='SendMessage'),
    path('v1/get_course_plan/', GetCoursePlan.as_view(), name='GetCoursePlan'),
    path('v1/create_course_plan/',
         CreateCoursePlan.as_view(), name='CreateCoursePlan'),
    path('v1/create_semester/', CreateSemester.as_view(), name='CreateSemester'),
    path('v1/post_course_plan/', PostCoursePlan.as_view(), name='PostCoursePlan'),
    path('v1/get_courses/', GetCourses.as_view(), name='GetCourses'),
]
