# Native imports
import json
# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes
# Importing user creation form
from accounts.forms.create_user import CustomUserCreationForm


class IsAuthorizedToCreateAdministrator(BasePermission):
    """
    Allows access only to authorized users. For testing the 
    permission is just for authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class CreateUserEngine():
    """
    Engine creates a standard for request processing, the 
    '__init__()' method saves the incoming request into 
    state and further checks for the 'utype' and runs the 
    method associated with it.
    """

    # The incoming request.
    request = None
    # The response to return to the view.
    response = None
    response_code = None
    # The user type to create
    utype = None
    # Credentials
    username = None
    email = None
    password1 = None
    password2 = None
    # The user
    user = None

    def __init__(self, params):
        # Loading defaults
        self.request = params
        try:
            self.utype = json.loads(params.body)['user_type']
            self.username = json.loads(params.body)['username']
            self.email = json.loads(params.body)['email']
            self.password1 = json.loads(params.body)['password1']
            self.password2 = json.loads(params.body)['password2']
        except KeyError:
            self.response = "Invalid Parameters"
            self.response_code = 400

        try:
            # Only use uppercase names for user methods
            getattr(self, self.utype.upper())()
        except AttributeError:
            self.response = "Invalid Parameters"
            self.response_code = 400

    def create_user(self, params):
        """
        Creates a user throught the custom user creation 
        form the parameters are passed through the parent 
        function.
        """
        f = CustomUserCreationForm(data=params)
        if f.is_valid():
            self.user = f.save()
            self.response = str(self.user) + " created, You can login now."
            self.response_code = 201
        else:
            self.response = str(f.errors)
            self.response_code = 500

    def CUSTOMER(self):
        """
        Customer users will be created with the username,
        email and the cleaned password. The profiles will 
        be created if the profile_data is provided in the
        request.
        """

        if self.username and self.email and self.password1 and self.password2:
            # Create user
            param = {
                "username": self.username,
                "email": self.email,
                "mode": 1,
                "password1": self.password1,
                "password2": self.password2
            }
            self.create_user(param)
        else:
            self.response = "Invalid Parameters"
            self.response_code = 400

    def VENDOR(self):
        """
        Vendors users will be created with the username,
        email and the cleaned password. The profiles will 
        be created if the profile_data is provided in the
        request.
        """
        if self.username and self.email and self.password1 and self.password2:
            # Create user
            param = {
                "username": self.username,
                "email": self.email,
                "mode": 2,
                "password1": self.password1,
                "password2": self.password2
            }
            self.create_user(param)
        else:
            self.response = "Invalid Parameters"
            self.response_code = 400

    def checkPerm(self):
        """
        Return True if the user is authenticated and has
        required permissions in this case permission to
        create an administrator account.
        """
        return (
            IsAuthenticated.has_permission(self, self.request, self) and
            IsAuthorizedToCreateAdministrator.has_permission(
                self, self.request, self)
        )

    def ADMINISTRATOR(self):
        # Since it's a protected view
        # Check for auth before responding.
        """
        Administrators users will be created with the 
        username, email and the cleaned password. The 
        profiles will be created if the profile_data is 
        provided in the request.
        """

        if self.checkPerm() == False:
            self.response = "You are not authorized"
            self.response_code = 401
            return

        if self.username and self.email and self.password1 and self.password2:
            # Create user
            param = {
                "username": self.username,
                "email": self.email,
                "mode": 3,
                "password1": self.password1,
                "password2": self.password2
            }
            self.create_user(param)
        else:
            self.response = "Internal Server Error"
            self.response_code = 500


class CreateUserView(APIView):
    permission_classes = ()

    def post(self, request):
        # Create the engine.
        Engine = CreateUserEngine(request)
        # Respond.
        return Response(Engine.response, Engine.response_code)

    def get(self, request):
        # Send testing response
        return Response(str(self.request.META['REMOTE_ADDR']))
