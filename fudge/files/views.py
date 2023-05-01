import magic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import UserFile
from .forms import UploadFileForm


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


def delete(request, file_id):
    UserFile.objects.get(pk=file_id).delete()
    return HttpResponseRedirect("/")
