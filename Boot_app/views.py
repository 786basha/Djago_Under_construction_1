from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Register

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    m = Register.objects.all()
    if request.method == "POST":
        a = request.POST['roll_i']
        b = request.POST['name_i']
        c = request.POST['mail_i']
        d = request.POST['age_i']
        p = Register(roll=a,name=b,mail=c,age=d)
        p.save()
        return redirect('/about')
    return render(request,'about.html',{'g':m})

def usrup(request,h):
    a = Register.objects.get(id=h)
    if request.method == "POST":
        a.roll = request.POST['roll_i']
        a.name = request.POST['name_i']
        a.mail = request.POST['mail_i']
        a.age = request.POST['age_i']
        a.save()
        return redirect('/about')
    return render(request,'usrup.html',{'t':a})

# def usrdel(request):
#     return render(request,'usrdel.html')

def usrdel(request,u):
	k = Register.objects.get(id=u)
	if request.method == "POST":
		k.delete()
		return redirect('/about')
	return render(request,'usrdel.html',{'p':k})
