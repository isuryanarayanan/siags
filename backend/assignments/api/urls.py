from ast import Sub
from django.urls import path
from assignments.api.get_assignments import GetAssignments
from assignments.api.submit_assignment import SubmitAssignment


urlpatterns = [
    path('v1/get_assignments/', GetAssignments.as_view(), name='GetAssignment'),
    path('v1/submit_assignment/', SubmitAssignment.as_view(),
         name='SubmitAssignment'),
]
