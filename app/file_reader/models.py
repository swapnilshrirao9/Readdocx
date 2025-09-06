from django.db import models
from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name.split("/")[-1]


class AudioLine(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="audio_lines")
    line_number = models.PositiveIntegerField()
    text = models.TextField()
    audio_file = models.FileField(upload_to="audio_lines/")

    def __str__(self):
        return f"{self.document} - Line {self.line_number}"

# Create your models here.
