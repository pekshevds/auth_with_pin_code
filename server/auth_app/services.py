from auth_app.models import CustomUser


def user_by_username(username: str) -> [CustomUser, None]:
    users = CustomUser.objects.filter(username=username)
    if users is None:
        return None
    return users.first()
