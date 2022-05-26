# Native imports
import json

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


# Local imports
from academy.models.plan import plan, planMessage
from academy.models.course import course
from academy.models.semester import semester


class sendMessageEngine():
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
            sender = params.user
            message = params.data.get("message")
            plan_id = params.data.get("plan_id")

            # create planMessage with params
            saveMessage = planMessage(sender=sender, message=message)
            saveMessage.save()

            # add plan message to plan
            savePlan = plan.objects.get(id=plan_id)
            savePlan.messages.add(saveMessage)
            savePlan.save()

            self.response = {"message": "hi"}
            self.response_code = 200

        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class sendMessage(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Create the engine.
        Engine = sendMessageEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
