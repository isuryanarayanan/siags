# Native imports
import json
from pyexpat.errors import messages
from unicodedata import name
import random
import string

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


# Local imports
from academy.models.plan import plan
from academy.models.course import course
from academy.models.semester import semester
from accounts.models.user import User


class CreateSemesterEngine():
    # The incoming request.
    request = None
    # The response to return to the view.
    response = None
    response_code = None
    course_plan = None

    def __init__(self, params):
        # Loading defaults
        self.request = params
        if True:
            user = params.user
            # check if user is a teacher
            if user.mode == 2:

                # create semester model
                self.semester = semester(
                    sem=params.data['sem'],
                )
                # self.semester.courses.set(params.data['courses'])
                # self.semester.electives.set(params.data['electives'])

                self.semester.save()
                # set params.data['courses'] to self.semester.courses
                for course_id in params.data['course']:
                    self.semester.courses.add(course_id)
                # set params.data['electives'] to self.semester.electives
                for elective_id in params.data['elective']:
                    self.semester.electives.add(elective_id)

                self.semester.save()
                # get plan where user is teacher and student is in params
                plan_list = plan.objects.filter(
                    teacher=user,
                    student=User.objects.get(id=params.data['student']),
                )
                # get first plan
                planx = plan_list[0]
                # add semester to plan
                planx.semesters.add(self.semester)
                # save plan
                planx.save()

                self.response_code = 200
                self.response = {
                    'message': 'Semester created successfully',
                    'semester_id': self.semester.id
                }

            else:
                self.response_code = 403
                self.response = "You are not a teacher."
                return

        else:
            self.response = "Invalid Parameters"
            self.response_code = 400

    def getCodeThatDontExist(self):
        # get all plans
        plans = plan.objects.all()
        # get all codes
        codes = [plan.code for plan in plans]
        # get a random code
        code = self.getRandomCode()
        # check if code already exists
        while code in codes:
            code = self.getRandomCode()
        # return code
        return code

    def getRandomCode(self):
        # get a random code
        code = ''.join(
            [random.choice(string.ascii_letters + string.digits) for n in range(10)])
        # return code
        return code


class CreateSemester(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        Engine = CreateSemesterEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
