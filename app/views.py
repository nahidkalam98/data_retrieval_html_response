from django.shortcuts import render

# Create your views here.

from app.models import *

from django.db.models.functions import Length

from django.db.models import Q

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
    
    QSWO = Webpage.objects.filter(Q(Topic_name='Cricket') & Q(Name__contains='v'))
    QSWO = Webpage.objects.filter(Q(Name__contains='v') | Q(url__regex='in$'))
     
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
    
    QSARO = AccessRecord.objects.filter(Q(Date__year__lte='2005') & Q(email__regex='\d+'))
    QSARO = AccessRecord.objects.filter(Q(Date__year='1998') | Q(email__contains='r'))
    

    
    
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


def update_webpage(request):
    
    #Webpage.objects.filter(Name='Gukesh D').update(url='https://dgukesh.in')
    #Webpage.objects.filter(Topic_name='Volleyball').update(Name='Abraham Minimol', url='http://minimol.a.in')
    #Webpage.objects.filter(Topic_name='Football').update(Name='Messi')
    #Webpage.objects.filter(Topic_name='Boxing').update(Name='Mary Kom')
    
    '''integrity error-foreign key constraint failed as boxing not in parent table'''
    #Webpage.objects.filter(Name='Virat Kohli').update(Topic_name='Boxing')
    
    #Webpage.objects.update_or_create(url='http://rnl.com', defaults={'Name':'Ronaldo'})
    
    '''Multiple objects returned as two data under football-- updation by update_or_create method will not be allowed'''
    #Webpage.objects.update_or_create(Topic_name='Football', defaults={'Name':'Neymar'})
    
    '''3 columns in table but value for only two provided'''
    #Webpage.objects.update_or_create(Name='Mary Kom', defaults={'url':'https://maryk.co.in'})
    
    '''Provide object when trying to update foreign key for already existing parent table value'''
    #Webpage.objects.update_or_create(Name='Magnus Carlsen', defaults={'Topic_name': 'Chess', 'url':'https://cmagnus.co.in'})
    
    CHTO = Topic.objects.get(Topic_name= 'Chess')    
    Webpage.objects.update_or_create(Name='Magnus Carlsen', defaults={'Topic_name': CHTO, 'url':'https://cmagnus.co.in'})

    
    QSWO = Webpage.objects.all()
    d = {'QSWO': QSWO}
    return render(request, 'display_webpage.html', d)


def delete_webpage(request):
    
    Webpage.objects.filter(Name = 'Gukesh D').delete()
    
    QSWO = Webpage.objects.all()
    d = {'QSWO': QSWO}
    return render(request, 'display_webpage.html', d)