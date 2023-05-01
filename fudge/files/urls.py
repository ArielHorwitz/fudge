from django.urls import path

from . import views

app_name = "files"
urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.upload, name="upload"),
    path("details/<int:file_id>/", views.details, name="details"),
    path('download/<int:file_id>/', views.download, name='download'),
    path("delete/<int:file_id>/", views.delete, name="delete"),
]
