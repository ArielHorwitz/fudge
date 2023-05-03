from functools import wraps
from pathlib import Path
import magic
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from .models import UserFile, ApiToken
from .forms import UploadFileForm


def check_token(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        try:
            user = ApiToken.objects.get(token=request.GET.get("token", "")).user
        except ApiToken.DoesNotExist:
            raise PermissionDenied()
        return f(request, *args, user=user, **kwargs)
    return wrapper


@check_token
def index(request, user):
    userfiles = UserFile.objects.filter(user__id=user.id)
    data = [dict(id=uf.id, name=uf.original_filename) for uf in userfiles]
    return JsonResponse(data)


@check_token
def download(request, user, file_id):
    userfile = get_object_or_404(UserFile, id=file_id)
    with open(userfile.file.path, "rb") as f:
        file_buffer = f.read()
    headers = {
        "Content-Type": magic.from_buffer(file_buffer, mime=True),
        "Content-Disposition": f'attachment; filename="{userfile.name}"',
    }
    return HttpResponse(file_buffer, headers=headers)


@check_token
def upload(request, user):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            userfile = UserFile(
                user=user,
                file=uploaded_file,
                original_filename=uploaded_file.name,
            )
            userfile.save()
            return JsonResponse({"success": True})
    else:
        form = UploadFileForm()
    return render(request, "files/upload.html", {"form": form})


@check_token
def delete(request, user, file_id):
    userfile = get_object_or_404(UserFile, id=file_id)
    Path(userfile.file.path).unlink()
    userfile.delete()
    return JsonResponse({"success": True})
