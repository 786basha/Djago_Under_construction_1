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

def Dtlup(request):
    p = Details.objects.all()
    return render(request,'Detail-up.html',{'k':p});

def DETAIL(request):
    p = Details.objects.all()
    if request.method == "POST":
        roll = request.POST.get('roll')
        name = request.POST.get('nam')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        addar = request.POST.get('addar') 
        pan = request.POST.get('pan')
        bacc = request.POST.get('bacc')
        bifsc = request.POST.get('bifsc')

        ds = Details(
            roll=roll,
            name=name,
            mail=mail,
            phone=phone,
            dob=dob,
            addar=addar,
            pan=pan,
            bacc=bacc,
            bifsc=bifsc
        )
        ds.save()
        return redirect('detail')
    return render(request,'Detail.html',{'k':p});

def UpDtl(request,id):
    m = Details.objects.all()
    if request.method == "POST":
        roll = request.POST.get('roll')
        name = request.POST.get('nam')
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        addar = request.POST.get('addar') 
        pan = request.POST.get('pan')
        bacc = request.POST.get('bacc')
        bifsc = request.POST.get('bifsc')

        ds1 = Details(
            id=id,
            roll=roll,
            name=name,
            mail=mail,
            phone=phone,
            dob=dob,
            addar=addar,
            pan=pan,
            bacc=bacc,
            bifsc=bifsc
        )
        ds1.save()
        return redirect('updtl')
    return render(request,'update-Dtl.html',{'k':m});
