from django.db import models
from django.contrib.auth.models import User


class UserFile(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    file = models.FileField(upload_to="files")
    original_filename = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.name} ({self.file.size} bytes)"

    @property
    def name(self):
        return self.original_filename
