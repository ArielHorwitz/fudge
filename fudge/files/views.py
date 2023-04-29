import magic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import UserFile


def index(request):
    all_files = list(UserFile.objects.all())
    context = dict(files=all_files)
    return render(request, "files/index.html", context)


def details(request, file_id):
    file = get_object_or_404(UserFile, pk=file_id)
    context = dict(file=file)
    return render(request, "files/details.html", context)


def download(request, file_id):
    userfile = UserFile.objects.get(pk=file_id)
    file_buffer = open(userfile.file.path, "rb").read()
    headers = {
        "Content-Type": magic.from_buffer(file_buffer, mime=True),
        "Content-Disposition": f'attachment; filename="{userfile.name}"',
    }
    return HttpResponse(file_buffer, headers=headers)
