import logging

from django.contrib.auth import get_user_model

from config import celery_app

logger = logging.getLogger(__name__)

User = get_user_model()


@celery_app.task()
def update_userinfo(
    email: str,
    username: str,
    first_name: str,
    last_name: str,
    is_superuser: bool,
    is_active: bool
):
    user = User.objects.get(username=username)

    context = {
        "email": email,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "is_superuser": is_superuser,
        "is_active": is_active
    }

    for field in [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_superuser",
        "is_active"
    ]:
        if getattr(user, field) != context[field]:
            setattr(user, field, context[field])

    user.save()
