from rest_framework_simplejwt import views as jwt_views
from django.urls import path, include
from accounts.views import TokenValidateView
urlpatterns = [
    path('api/', include('accounts.api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/validate/', TokenValidateView.as_view())
]
