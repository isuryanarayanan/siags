# Native imports
import json

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


# Local imports
from academy.models.plan import plan
from academy.models.course import course
from academy.models.semester import semester


class GetCoursePlanEngine():
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

            course_plan = plan.objects.filter(student=user)

            # from course_plan semesters get all corresponding semester objects
            semesters = []
            for plan_semester in course_plan[0].semesters.all():
                semesters.append(semester.objects.get(id=plan_semester.id))

            # from semester get all corresponding course objects
            courses = []
            for sem in semesters:
                for course in sem.courses.all():
                    courses.append(course)

            self.response = {
                "course_plan": {
                    "name": course_plan[0].name,
                    "code": course_plan[0].code,
                    "description": course_plan[0].description,
                    "semesters": [
                        {
                            "sem": semester.sem,
                            "courses": [
                                {
                                    "name": course.name,
                                    "code": course.code,
                                    "description": course.description,
                                    "elective": course.elective,
                                    "credits": course.credits,
                                    "prerequisite": [
                                        course.prerequisite.all()
                                    ]
                                } for course in semester.courses.all()
                            ],
                            "electives": [
                                {
                                    "name": course.name,
                                    "code": course.code,
                                    "description": course.description,
                                    "elective": course.elective,
                                    "credits": course.credits,
                                    "prerequisite": [
                                        course.prerequisite.all()
                                    ]
                                } for course in semester.electives.all()
                            ]
                        } for semester in semesters
                    ]
                }

            }
            self.response_code = 200

        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class GetCoursePlan(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        Engine = GetCoursePlanEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
