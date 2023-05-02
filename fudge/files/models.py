from pathlib import Path
from django.db import models
from django.contrib.auth.models import User


class UserFile(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    file = models.FileField(upload_to="files")

    def __str__(self):
        return f"{self.name} ({self.file.size} bytes)"

    @property
    def name(self):
        return Path(self.file.name).name
