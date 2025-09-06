from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import csv

def upload_file(request):
    content = None
    if request.method == "POST" and request.FILES["file"]:
        uploaded_file = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(filename)

        # Example: Read text or CSV
        if filename.endswith(".txt"):
            with open(file_path, "r") as f:
                content = f.read()
        elif filename.endswith(".csv"):
            with open(file_path, newline="") as f:
                reader = csv.reader(f)
                content = list(reader)

    return render(request, "file_reader/upload.html", {"content": content})

