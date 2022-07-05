from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserView, UserApiView, UserLogoutView, UserInfoView

urlpatterns = [
    path('', UserView.as_view()),
    # path('api/token/', UserApiView.as_view(), name='login'),
    path('api/userinfo/', UserInfoView.as_view(), name='userinfo'),
    path('api/logout/', UserLogoutView.as_view(), name='logout'),
    path('api/signup/', UserView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
