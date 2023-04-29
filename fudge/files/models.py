from pathlib import Path
from django.db import models


class UserFile(models.Model):
    file = models.FileField(upload_to="files")

    def __str__(self):
        return f"{self.name} ({self.file.size} bytes)"

    @property
    def name(self):
        return Path(self.file.name).name
