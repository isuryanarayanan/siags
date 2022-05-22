# Native imports
import json
# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import permission_classes


class TokenValidateView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(str(self.request.META['REMOTE_ADDR']))
