# Native imports
import json

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


# Local imports
from assignments.models import Assignment


class GetAssignmentsEngine():
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

            # in all assignments check if user is in assigned_to field
            if user.mode == 1:
                assignments = Assignment.objects.filter(assigned_to=user)
            else:
                assignments = Assignment.objects.filter(owner=user)

            self.response = {
                "assignments": [
                    {
                        "id": assignment.id,
                        "title": assignment.title,
                        "description": assignment.description,
                        "due_date": assignment.due_date,
                        "created_at": assignment.created_at,
                        "updated_at": assignment.updated_at,
                        "owner": assignment.owner.username,
                        "assigned_to": [
                            user.username for user in assignment.assigned_to.all()
                        ]
                    } for assignment in assignments
                ]

            }
            self.response_code = 200

        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class GetAssignments(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        Engine = GetAssignmentsEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
