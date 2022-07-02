# Native imports
import json
from unicodedata import name

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


# Local imports
from academy.models.plan import plan
from academy.models.course import course
from academy.models.semester import semester


class PostCoursePlanEngine():
    # The incoming request.
    request = None
    # The response to return to the view.
    response = None
    response_code = None
    course_plan = None

    def __init__(self, params):
        # Loading defaults
        self.request = params
        try:
            user = params.user
            # check if user is a teacher
            if user.mode == 2:

                # get semester details from request
                semesters = params.data['semesters']

                # for each semester in semesters create the model and save the id
                semester_ids = []
                for semester in semesters:
                    semester_obj = semester(
                        sem=semester['sem'],
                        courses=semester['courses'],
                        electives=semester['electives']
                    )
                    semester_obj.save()
                    semester_ids.append(semester_obj.id)

                # create the plan
                self.course_plan = plan(
                    name=params.data['name'],
                    code=params.data['code'],
                    description=params.data['description'],
                    teacher=user,
                    student=User.objects.get(id=params.data['student']),
                    semesters=semester_ids
                )
                self.course_plan.save()

                self.response_code = 200
                self.response = {
                    'message': 'Plan created successfully',
                    'plan_id': self.course_plan.id
                }
            else:
                self.response_code = 403
                self.response = "You are not a teacher."
                return

        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class PostCoursePlan(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        Engine = PostCoursePlanEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
