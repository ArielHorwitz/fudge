from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

import secrets
import string


TOKEN_CHARS = string.ascii_letters + string.digits


class UserFile(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    file = models.FileField(upload_to="files")
    original_filename = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name} ({self.file.size} bytes)"

    @property
    def name(self):
        return self.original_filename


class ApiToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=2048)

    @classmethod
    def generate_random(cls, user):
        new_token = ''.join(secrets.choice(TOKEN_CHARS) for i in range(64))
        return cls(user=user, token=new_token)

    def __str__(self):
        return f"<ApiToken '{self.token[:6]}'>"
