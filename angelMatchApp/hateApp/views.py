from django.http import HttpResponse, HttpResponseRedirect
#from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .models import hateApp

# Create your views here.

def index(request):
    mymembers = hateApp.objects.all().values()
    template = loader.get_template('index.html')
    context={
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))
def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    h = request.POST['hatefood']
    a = request.POST['age']
    member = hateApp(firstname = x, lastname = y, hatefood = h, age = a)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = hateApp.objects.get(id = id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = hateApp.objects.get(id = id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    hate = request.POST['hatefood']
    age = request.POST['age']
    
    member = hateApp.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.hatefood = hate
    member.age = age
    member.save()
    return HttpResponseRedirect(reverse('index'))

def testing(request):
    mymembers = hateApp.objects.all().values()
    template = loader.get_template('template.html')
    context={
        'mymembers' : mymembers,
    }
       # creates a variable 'firstname' : 'Christian'

    return HttpResponse(template.render(context,request))
def dating(request):
    mymembers = hateApp.objects.all().values()
    template = loader.get_template("dating.html")
    context={
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context,request))
    #output = ""
    #or x in mymembers:
     #   output += x["firstname"]
    #return HttpResponse(output)
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    
    #return HttpResponse("Hello Angel!")
