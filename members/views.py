from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.
def index(request):
    mymembers=Members.objects.all().values()
    template=loader.get_template('myfirst.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))


def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    member=Members(firstname=x,lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))
def delete(request,id):
    x=Members.objects.get(id=id)
    x.delete()
    return HttpResponseRedirect(reverse('index'))
def edit(request,id):
    member=Members.objects.get(id=id)
    template=loader.get_template('edit.html')
    context={
        'member':member
    }
    return HttpResponse(template.render(context,request))
def editrecord(request,id):
    member=Members.objects.get(id=id)
    member.firstname=request.POST['first']
    member.lastname=request.POST['last']
    member.save()
    return HttpResponseRedirect(reverse(index))

