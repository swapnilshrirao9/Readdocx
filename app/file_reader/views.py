import os
import docx
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.base import ContentFile
from django.http import JsonResponse
from gtts import gTTS

from .models import Document, AudioLine


def upload_file(request):
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        doc = Document.objects.create(file=uploaded_file)

        # Extract text line by line
        if uploaded_file.name.endswith(".docx"):
            doc_path = doc.file.path
            parsed_doc = docx.Document(doc_path)
            lines = [p.text.strip() for p in parsed_doc.paragraphs if p.text.strip()]

            for idx, line in enumerate(lines, start=1):
                tts = gTTS(text=line, lang="en")
                filename = f"{doc.id}_line_{idx}.mp3"
                filepath = os.path.join(settings.MEDIA_ROOT, "audio_lines", filename)
                os.makedirs(os.path.dirname(filepath), exist_ok=True)
                tts.save(filepath)

                AudioLine.objects.create(
                    document=doc,
                    line_number=idx,
                    text=line,
                    audio_file=f"audio_lines/{filename}"
                )

        return redirect("list_files")
    return render(request, "upload.html")


def list_files(request):
    documents = Document.objects.all().order_by("-uploaded_at")
    return render(request, "list.html", {"documents": documents})


def detail_file(request, pk):
    document = get_object_or_404(Document, pk=pk)
    lines = document.audio_lines.all().order_by("line_number")
    return render(request, "detail.html", {"document": document, "lines": lines})
