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





def Insert_Topic(request):
    tn = input('Enter Topic_name : ')
    to = Topic.objects.get_or_create(Topic_name=tn)[0]
    to.save()
    
    QSTO = Topic.objects.all()
    d = {'QSTO': QSTO}
    return render(request, 'display_topics.html', context = d)


def Insert_Webpage(request):
    tn = input('Enter Topic_name : ')
    to = Topic.objects.get(Topic_name=tn)
    
    n = input('Enter Name : ')
    u = input('Enter url : ')
    wo = Webpage.objects.get_or_create(Topic_name = to, Name = n, url = u)[0]
    wo.save()
    
    QSWO = Webpage.objects.all()
    d = {'QSWO': QSWO}
    return render(request, 'display_webpage.html', d)
 
 
    

def Insert_AC(request):
    tn = input('Enter Topic_name : ')
    to = Topic.objects.get(Topic_name=tn)
    to.save()
    pk= input('Enter pk value : ')
    n = input('Enter Name : ')
    u = input('Enter url : ')
    wo = Webpage.objects.get(pk=pk)
   
    d = input('Enter Date : ')
    a = input('Enter Author : ')
    e = input('Enter email : ')
    ao = AccessRecord.objects.get_or_create(Name=wo, Date=d, Author=a, email=e)[0]
    ao.save()
    
    QSARO = AccessRecord.objects.all()
    d = {'QSARO': QSARO}
    return render(request, 'display_AR.html', d)