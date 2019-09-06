from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import HDFSBrowserForm
from .functions import handle_uploaded_file


@login_required
def fileBrowser(request):
    if request.method == 'POST':
        files = HDFSBrowserForm(request.POST, request.FILES)
        if files.is_valid():
            handle_uploaded_file(request.FILES['file']) 
            messages.success(request, f'Load datas success')
            return redirect('filebrowser')
    else:
        files = HDFSBrowserForm()
    return render(request, 'browser/index.html', {'form': files})

