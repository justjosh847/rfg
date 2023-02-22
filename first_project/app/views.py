import datetime
import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    template_name = 'app/home.html'
    msg = f'app/home.html: {template_name}'
    pages = {
        'app/home.html': reverse('home'),
        'app/time.html': reverse('time'),
        'app/workdir.html': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time()
    msg = f' {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    workdir = os.listdir()
    msg = f' {workdir}'
    return HttpResponse(msg)
    raise NotImplemented
