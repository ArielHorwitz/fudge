from django.urls import path

from . import views
from . import api_v1

app_name = "files"
urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.upload, name="upload"),
    path("details/<int:file_id>/", views.details, name="details"),
    path('download/<int:file_id>/', views.download, name='download'),
    path("delete/<int:file_id>/", views.delete, name="delete"),
    path("generate-api-token/", views.generate_api_token, name="gen_api_token"),
    path("api/v1/index/", api_v1.index),
    path("api/v1/upload/", api_v1.upload),
    path("api/v1/download/<int:file_id>/", api_v1.download),
    path("api/v1/delete/<int:file_id>/", api_v1.delete),
]
