from pathlib import Path
import magic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import UserFile
from .forms import UploadFileForm


@login_required
def index(request):
    all_files = list(UserFile.objects.all())
    context = dict(files=all_files)
    return render(request, "files/index.html", context)


@login_required
def details(request, file_id):
    userfile = get_object_or_404(UserFile, pk=file_id)
    try:
        preview = open(userfile.file.path).read()[:1000]
    except UnicodeDecodeError:
        preview = "No preview available."
    context = dict(file=userfile, preview=preview)
    return render(request, "files/details.html", context)


@login_required
def download(request, file_id):
    userfile = get_object_or_404(UserFile, pk=file_id)
    file_buffer = open(userfile.file.path, "rb").read()
    headers = {
        "Content-Type": magic.from_buffer(file_buffer, mime=True),
        "Content-Disposition": f'attachment; filename="{userfile.name}"',
    }
    return HttpResponse(file_buffer, headers=headers)


@login_required
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            userfile = UserFile(file=uploaded_file)
            userfile.save()
            return HttpResponseRedirect("/")
    else:
        form = UploadFileForm()
    return render(request, "files/upload.html", {"form": form})


@login_required
def delete(request, file_id):
    userfile = get_object_or_404(UserFile, pk=file_id)
    Path(userfile.file.path).unlink()
    userfile.delete()
    return HttpResponseRedirect("/")
