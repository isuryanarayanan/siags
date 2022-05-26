# Native imports
import json

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes
from rest_framework.parsers import FileUploadParser, MultiPartParser


# Local imports
from assignments.models import Assignment, AssignmentSubmission


class SubmitAssignmentEngine():
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
            # print request in readable format

            # create an assignment submission with the file
            assignment_submission = AssignmentSubmission(
                assignment=Assignment.objects.get(
                    id=params.data['assignment_id']),
                student=user,
                file=params.data['file']
            )
            assignment_submission.save()

            self.response = {
                "id": assignment_submission.id,
                "assignment": assignment_submission.assignment.id,
                "student": assignment_submission.student.username,
                "created_at": assignment_submission.created_at,
                "updated_at": assignment_submission.updated_at,
                "file": assignment_submission.file.url
            }
            self.response_code = 200

        except Exception as e:
            print(e)
            self.response = "Invalid Parameters"
            self.response_code = 400


class SubmitAssignment(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        # Create the engine.
        Engine = SubmitAssignmentEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
