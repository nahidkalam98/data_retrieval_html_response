from django.shortcuts import render

# Create your views here.

from app.models import *

def display_topics(request):
    QSTO = Topic.objects.all()
    d = {'QSTO': QSTO}
    return render(request, 'display_topics.html', context = d)

def display_webpage(request):
    QSWO = Webpage.objects.all()
    d = {'QSWO': QSWO}
    return render(request, 'display_webpage.html', d)

def display_AR(request):
    QSARO = AccessRecord.objects.all()
    d = {'QSARO': QSARO}
    return render(request, 'display_AR.html', d)
