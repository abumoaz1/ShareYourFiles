from django.shortcuts import render, redirect
from .forms import FileUploadForm
from django.contrib.auth.decorators import login_required
from .models import FileUpload

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.user = request.user
            file_instance.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})

def file_list(request):
    files = FileUpload.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})

def home(request):
    return render(request, 'home.html', {'home': home})
