# Native imports
import json
# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


class IsCustomerUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user.mode == 1)


class CustomerProfileEngine():
    """
    Customer profile engine allows users to set fields in their
    profile. Basically and endpoint for anything to do with your 
    profile.
    """

    # The incoming request.
    request = None
    # The response to return to the view.
    response = None
    response_code = None

    def __init__(self, params):
        # Loading defaults
        self.request = params
        try:
            # Load params here
        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400

        try:
            # Only use uppercase names for user methods
            getattr(self, self.utype.upper())()
        except AttributeError:
            self.response = "Invalid Parameters"
            self.response_code = 400


class SetCustomerProfileView(APIView):
    permission_classes = (IsAuthenticated, IsCustomerUser)

    def post(self, request):
        # Create the engine.
        Engine = CustomerProfileEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
