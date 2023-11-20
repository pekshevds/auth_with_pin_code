from django.urls import path
from auth_app.views import CustomSignInView
from auth_app.views import CustomSignUpView
from auth_app.views import CustomSignOutView

app_name = 'auth_app'

urlpatterns = [
    path('sign-in/', CustomSignInView.as_view(), name="sign-in"),
    path('sign-up/', CustomSignUpView.as_view(), name="sign-up"),
    path('sign-out/', CustomSignOutView.as_view(), name="sign-out"),
]
