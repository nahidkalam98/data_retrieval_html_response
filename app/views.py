from django.shortcuts import render

# Create your views here.

from app.models import *

from django.db.models.functions import Length

def display_topics(request):
    QSTO = Topic.objects.all()
    
    QSTO = Topic.objects.exclude(Topic_name='Cricket').order_by(Length('Topic_name'))
    QSTO = Topic.objects.all().order_by('Topic_name')
    QSTO = Topic.objects.all().order_by('-Topic_name')
    QSTO = Topic.objects.all().order_by(Length('Topic_name'))
    QSTO = Topic.objects.all().order_by(Length('Topic_name').desc())
    
    QSTO = Topic.objects.filter(Topic_name__startswith='c')
    QSTO = Topic.objects.filter(Topic_name__endswith='ball')
    QSTO = Topic.objects.filter(Topic_name__contains='b')

    
    d = {'QSTO': QSTO}
    return render(request, 'display_topics.html', context = d)


def display_webpage(request):
    QSWO = Webpage.objects.all()
    
    QSWO = Webpage.objects.exclude(Topic_name='Cricket').order_by(Length('Topic_name'))
    QSWO = Webpage.objects.all().order_by('Name')
    QSWO = Webpage.objects.all().order_by('-Name')
    QSWO = Webpage.objects.all().order_by(Length('Name'))
    QSWO = Webpage.objects.all().order_by(Length('Name').desc())
    QSWO = Webpage.objects.all()[:5:1]
    
    QSWO = Webpage.objects.exclude(Name__startswith='v')
    QSWO = Webpage.objects.exclude(Name__endswith='i')
    QSWO = Webpage.objects.filter(url__regex='in$')
    QSWO = Webpage.objects.filter(Name__regex='^v')
    QSWO = Webpage.objects.filter(Name__regex='^V')
     
    d = {'QSWO': QSWO}
    return render(request, 'display_webpage.html', d)

def display_AR(request):
    QSARO = AccessRecord.objects.all()
    
    QSARO = AccessRecord.objects.all().order_by('Date')
    QSARO = AccessRecord.objects.all().order_by('-Date')
    QSARO = AccessRecord.objects.all().order_by(Length('Author'))
    QSARO = AccessRecord.objects.all().order_by(Length('Author').desc())
    QSARO = AccessRecord.objects.all()[0:5:1]
    
    QSARO = AccessRecord.objects.filter(Author__in=('GD', 'SD', 'MSD', 'VK'))
    QSARO = AccessRecord.objects.filter(Date__day='12')
    QSARO = AccessRecord.objects.filter(Date__month='05')
    QSARO = AccessRecord.objects.filter(Date__year='2023')
    
    QSARO = AccessRecord.objects.filter(Date__year__gte='2020')
    QSARO = AccessRecord.objects.filter(Date__lte='2020-01-01')
    QSARO = AccessRecord.objects.filter(Date__year__gt='2005')
    QSARO = AccessRecord.objects.filter(Date__gt='2022-11-01')
    
    QSARO = AccessRecord.objects.filter(Author__contains='a')
    QSARO = AccessRecord.objects.filter(email__regex='\w*[.]\w+@gmail[.]com')
    
    
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