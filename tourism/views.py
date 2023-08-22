import email
import http
from re import template
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Tourism
from django_tourism.settings import EMAIL_HOST_USER

from django.core.mail import send_mail
# Create your views here.

def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())
def goa(request):
    template=loader.get_template('goa.html')
    return HttpResponse(template.render())
def lehladkah(request):
    template=loader.get_template('lehladkah.html')
    return HttpResponse(template.render())
def kerela(request):
    template=loader.get_template('kerela.html')
    return HttpResponse(template.render())
def andaman(request):
    template=loader.get_template('andaman.html')
    return HttpResponse(template.render())
def dubai(request):
    template=loader.get_template('dubai.html')
    return HttpResponse(template.render())
def singapore(request):
    template=loader.get_template('singapore.html')
    return HttpResponse(template.render())
def maldives(request):
    template=loader.get_template('maldives.html')
    return HttpResponse(template.render())
def thailand(request):
    template=loader.get_template('thailand.html')
    return HttpResponse(template.render())

'''def table(request):
    mymembers=Members.objects.all().values()
    template=loader.get_template('table.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))'''
def ttable(request):
    customer=Tourism.objects.all().values()
    template=loader.get_template('ttable.html')
    context={
        'customer':customer,
    }
    return HttpResponse(template.render(context,request))
def homeadd(request):
    template=loader.get_template('homeadd.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    # a=request.POST['from']
    # b=request.POST['to']
    # c=request.POST['ddate']
    # d=request.POST['rdate']
    # e=request.POST['adult']
    # f=request.POST['child']
    # g=request.POST['email']
    # h=request.FILES['image_x']

    a=request.GET.get('from')
    b=request.GET.get('to')
    c=request.GET.get('ddate')
    d=request.GET.get('rdate')
    e=request.GET.get('adult')
    f=request.GET.get('child')
    g=request.GET.get('email')
    h=request.GET.FILES['image_x']
    tourism=Tourism(fromm=a,to=b,departure=c,returnn=d,adult=e,child=f,email=g,image_x=h)
    tourism.save()
    # send_mail('Welcome to Django Tourism ',f' Booking Details \n\n From - {a}   To - {b}\n Departure Date -  {c}   Return Date -  {d}\n Number of Passengers: Adults - {e}  Childs - {f} \n\n\n Wish you a happy journey !!','vip2121206@sicsr.ac.in',[g])
    return HttpResponseRedirect('/ttable')
def delete(request,id):
    tourism=Tourism.objects.get(id=id)
    tourism.delete()
    return HttpResponseRedirect('/ttable')
def update(request,id):
    customer=Tourism.objects.get(id=id)
    template=loader.get_template('homeupdate.html')
    context={
        'customer':customer,
    }
    return HttpResponse(template.render(context,request))
def homeupdate(request,id):
    a=request.POST['from']
    b=request.POST['to']
    c=request.POST['ddate']
    d=request.POST['rdate']
    e=request.POST['adult']
    f=request.POST['child']
    g=request.POST['email']
    customer=Tourism.objects.get(id=id)
    customer.fromm=a
    customer.to=b
    customer.departure=c
    customer.returnn=d
    customer.adult=e
    customer.child=f
    customer.email=g
    customer.save()
    send_mail('Welcome to Django Tourism ',f' Your booking is UPDATED!\n \n From - {a}   To - {b}\n Departure Date -  {c}   Return Date -  {d}\n Number of Passengers: Adults - {e}  Childs - {f} \n\n\n Wish you a happy journey !!','vip2121206@sicsr.ac.in',[g])
    return HttpResponseRedirect('/ttable')
