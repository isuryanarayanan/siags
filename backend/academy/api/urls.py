from django.urls import path
from academy.api.get_courseplan import GetCoursePlan
from academy.api.send_message import sendMessage


urlpatterns = [
    path('v1/get_course_plan/', GetCoursePlan.as_view(), name='GetCoursePlan'),
    path('v1/send_message/', sendMessage.as_view(), name='SendMessage'),
]
