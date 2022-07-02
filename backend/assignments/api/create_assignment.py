# Native imports
import json
from turtle import title

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


# Local imports
from assignments.models import Assignment
from academy.models.batch import batch


class CreateAssignementEngine():
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

            if user.mode == 2:
                # create the assignment model
                assignment = Assignment(
                    title=params.data['title'],
                    description=params.data['description'],
                    due_date=params.data['due_date'],
                    created_at=params.data['created_at'],
                    updated_at=params.data['updated_at'],
                    owner=user,
                )

                assignment.save()

                # get batch using batch id
                batch_id = params.data['batch_id']
                batch_obj = batch.objects.get(id=batch_id)

                # get all batch students
                students = batch_obj.students.all()

                # assign to all students
                for student in students:
                    assignment.assigned_to.add(student)

                # return success message
                self.response = {
                    'message': 'Assignment created successfully',
                    'assignment': assignment.id
                }
                self.response_code = 200

        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class CreateAssignement(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        Engine = CreateAssignementEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
