from django.urls import path, include
from .create_user import CreateUserView
from .get_user import GetUserView
from .handshake import HandshakeView

urlpatterns = [
    path('create_user/', CreateUserView.as_view(), name='CreateUserView'),
    path('get_user/', GetUserView.as_view(), name='GetUserView'),
    path('handshake/', HandshakeView.as_view(), name='HandshakeView')
]
