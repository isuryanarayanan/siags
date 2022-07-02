# Native imports
import json

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


# Local imports
from academy.models.plan import plan
from academy.models.batch import batch
from academy.models.course import course
from academy.models.semester import semester


class GetCoursesEngine():
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
            course_list = course.objects.all()

            if not course_list:
                self.response_code = 404
                self.response = {
                    "message": "No courses found."
                }
                return
            else:
                self.response_code = 200
                self.response = {
                    "course_list": [
                        {
                            "id": course.id,
                            "name": course.name,
                            "description": course.description,
                            "elective": course.elective,
                            "credits": course.credits,
                            "prerequisite": course.prerequisite.all()
                        }
                        for course in course_list
                    ]
                }
                return

        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class GetCourses(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        # add key to request
        Engine = GetCoursesEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)
