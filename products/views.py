from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoadLogsForm


@login_required
def word_count(request):
    return render(request, 'word_count/index.html', {'title': 'word_count'})

@login_required
def weblog(request):
    if request.method == 'POST':
        form = LoadLogsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Load datas success')
    else:
        form = LoadLogsForm()
    return render(request, 'weblog/index.html', {'form': form})


@login_required
def taxi_nyc(request):
    return render(request, 'taxi_nyc/index.html', {'title': 'taxi_nyc'})