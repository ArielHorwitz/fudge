from django.urls import path

from . import views

app_name = "files"
urlpatterns = [
    path("", views.index, name="index"),
    path("details/<int:file_id>/", views.details, name="details"),
    path('download/<int:file_id>/', views.download, name='download'),
]
