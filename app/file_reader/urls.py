from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_file, name="upload_file"),
    path("files/", views.list_files, name="list_files"),
    path("files/<int:pk>/", views.detail_file, name="detail_file"),
]
