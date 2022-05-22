from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json


class HandshakeView(APIView):
    permission_classes = ()

    def get(self, request):

        content = {
            "handshake": True
        }

        # Evaluate handshake here

        return Response(content)
