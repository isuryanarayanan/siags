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


class GetBatchEngine():
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

            # return students in batch of authenticated user as teacher
            batch_list = batch.objects.filter(teacher=user)

            # respond with student list of batch
            if not batch_list:
                self.response_code = 404
                self.response = {
                    "message": "No batch found for this user."
                }
                return
            else:
                self.response_code = 200
                self.response = {
                    "batch_list": [
                        {
                            "id": batch.id,
                            "teacher": batch.teacher.username,
                            "students": [
                                {
                                    "id": student.id,
                                    "username": student.username
                                }
                                for student in batch.students.all()
                            ]
                        }
                        for batch in batch_list
                    ]
                }
                return

        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class GetBatch(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Create the engine.
        Engine = GetBatchEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)
