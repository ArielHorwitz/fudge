from pathlib import Path
import magic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import UserFile, ApiToken
from .forms import UploadFileForm


@login_required
def index(request):
    userfiles = UserFile.objects.filter(user__id=request.user.id)
    context = dict(files=userfiles)
    return render(request, "files/index.html", context)


@login_required
def details(request, file_id):
    userfile = get_object_or_404(UserFile, id=file_id)
    try:
        with open(userfile.file.path) as f:
            preview = str(f.read())[:1000]
    except UnicodeDecodeError:
        preview = "No preview available."
    context = dict(file=userfile, preview=preview)
    return render(request, "files/details.html", context)


@login_required
def download(request, file_id):
    userfile = get_object_or_404(UserFile, id=file_id)
    with open(userfile.file.path, "rb") as f:
        file_buffer = f.read()
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
            userfile = UserFile(
                user=request.user,
                file=uploaded_file,
                original_filename=uploaded_file.name,
            )
            userfile.save()
            return HttpResponseRedirect("/")
    else:
        form = UploadFileForm()
    return render(request, "files/upload.html", {"form": form})


@login_required
def delete(request, file_id):
    userfile = get_object_or_404(UserFile, id=file_id)
    Path(userfile.file.path).unlink()
    userfile.delete()
    return HttpResponseRedirect("/")


@login_required
def generate_api_token(request):
    ApiToken.objects.filter(user=request.user).delete()
    new_token = ApiToken.generate_random(request.user)
    new_token.save()
    return render(request, "files/api-token.html", dict(token=new_token.token))
