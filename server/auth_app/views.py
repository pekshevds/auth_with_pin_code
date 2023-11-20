from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.views import View
from pin_app.services import (
    add_record,
    not_used_users_record_by_pin_code,
    not_used_users_records,
    use_record
)
from auth_app.services import user_by_username


class CustomSignUpView(View):
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", "")
        user = user_by_username(username=username)
        if user is None:
            return render(
                request=request,
                template_name="auth_app/signin.html"
            )

        pin_code = request.POST.get("pin_code", "")

        records = not_used_users_records(user=user)
        record = not_used_users_record_by_pin_code(
            records=records,
            pin_code=pin_code
        )

        if record is None:
            return render(
                request=request,
                template_name="auth_app/signin.html"
            )

        password = settings.AUTH_USER_DEFAULT_PASSWORD
        auth_user = authenticate(
            request=request,
            username=username,
            password=password
        )
        print("auth_user=", auth_user)
        if auth_user is None:
            return render(
                request=request,
                template_name="auth_app/signin.html"
            )

        login(request, auth_user)
        use_record(record=record)
        return render(
                request=request,
                template_name="auth_app/index.html"
            )


class CustomSignOutView(View):
    def get(self, request, *args, **kwargs):
        logout()


class CustomSignInView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="auth_app/signin.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username", "")
        user = user_by_username(username=username)
        if user is None:
            return render(
                request=request,
                template_name="auth_app/signin.html"
            )

        add_record(user=user)
        return render(
            request=request,
            template_name="auth_app/signup.html",
            context={"user": user}
        )
