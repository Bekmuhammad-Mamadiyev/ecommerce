from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('verify-otp/', VerifyOtpView.as_view(), name='verify-otp'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-password/start/', ResetPasswordStartView.as_view(), name='reset-password-start'),
    path('reset-password/finish/', ResetPasswordFinishView.as_view(), name='reset-password-finish'),
]

