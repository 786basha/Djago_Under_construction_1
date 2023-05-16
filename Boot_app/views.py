from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import *

# Create your views here.

def home1(request):
    emp = Register.objects.all()
    return render(request,'index.html',{'emp':emp});

def add(request):
    k = Register.objects.all()
    if request.method=='POST':
        roll = request.POST.get('roll')
        name = request.POST.get('nam')
        mail = request.POST.get('mail')
        address = request.POST.get('address')
        backlog = request.POST.get('backlog')

        emp = Register(
            roll = roll,
            name = name,
            mail = mail,
            address = address,
            backlog = backlog,
        )
        emp.save()
        return redirect('home')
    return render(request,'index.html',{'emp':k})

def edit(request):
    emp = Register.objects.all()

    context = {
        'emp' : emp,
    }
    return render(request,'index.html',context)

def update(request,h):
    
    if request.method == 'POST':
        roll = request.POST.get('roll')
        name = request.POST.get('nam')
        mail = request.POST.get('mail')
        address = request.POST.get('address')
        backlog = request.POST.get('backlog')
        emp = Register(
            id = h,
            roll = roll,
            name = name,
            mail = mail,
            address = address,
            backlog = backlog,
        )
        emp.save()
        return redirect('home')
    return render(request,'index.html')

def DELETE(request,d):
    emp = Register.objects.get(id=d).delete()

    context = {
        'emp' : emp,
    }

    return redirect('home')
    return render(request,'index.html',context)
