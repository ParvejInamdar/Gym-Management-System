from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *

# Create your views here.
def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    enquirys=Enquiry.objects.all()
    plans=Plan.objects.all()
    equipments=Equipment.objects.all()
    members=Member.objects.all()
    e1 = 0
    p1 = 0
    eq1 = 0
    m1 = 0
    for i in enquirys:
        e1+=1
    for i in plans:
        p1+=1
    for i in equipments:
        eq1+=1
    for i in members:
        m1+=1
    d = {'e1':e1,'p1':p1,'eq1':eq1,'m1':m1} 
    return render(request,"index.html",d)

def Login(request):
    error = ""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="No"
            else:
                error="Yes"
        except:
            error="Yes"
    d = {'error': error}
    return render(request,"login.html",d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect("login")

def Add_Enquiry(request):
    error =""
    if not request.user.is_staff:
        return redirect('login')
    #Fetching all data from Enquiry model into enq variable
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(name=n,contact=c,emailid=e,age=a,gender=g)
            error = "No"
        except:
            error = "Yes"
    d = {'error':error}        
    return render(request,"add_enquiry.html",d)

def View_Enquiry(request):
    if not request.user.is_staff:
        return redirect('login')
    enq = Enquiry.objects.all()
    d = {'enq':enq}
    return render(request,"view_enquiry.html",d)

def Delete_Enquiry(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect("view_enquiry")


def Add_Equipment(request):
    error =""
    if not request.user.is_staff:
        return redirect('login')
    #Fetching all data from Enquiry model into enq variable
    if request.method=="POST":
        n = request.POST['ename']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        des = request.POST['description']
        try:
            Equipment.objects.create(name=n,price=p,unit=u,date=d,description=des)
            error = "No"
        except:
            error = "Yes"
    d = {'error':error}        
    return render(request,"add_equipment.html",d)

def View_Equipment(request):
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.all()
    d = {'equipment':equipment}
    return render(request,"view_equipment.html",d)

def Delete_Equipment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect("view_equipment")

def Add_Plan(request):
    error =""
    if not request.user.is_staff:
        return redirect('login')
    #Fetching all data from Enquiry model into enq variable
    if request.method=="POST":
        n = request.POST['name']
        am = request.POST['amount']
        du = request.POST['duration']
        try:
            Plan.objects.create(name=n,amount=am,duration=du)
            error = "No"
        except:
            error = "Yes"
    d = {'error':error}        
    return render(request,"add_plan.html",d)

def View_Plan(request):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.all()
    d = {'plan':plan}
    return render(request,"view_plan.html",d)

def Delete_Plan(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect("view_plan")

def Add_Member(request):
    error =""
    if not request.user.is_staff:
        return redirect('login')
    #Fetching all data from Enquiry model into enq variable
    if request.method=="POST":
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        j = request.POST['joindate']
        ex = request.POST['expireddate']
        ia = request.POST['initialamount']
        try:
            Member.objects.create(name=n,contact=c,emailid=e,age=a,gender=g,plan=p,joindate=j,expireddate=ex,initialamount=ia)
            error = "No"
        except:
            error = "Yes"
    d = {'error':error}        
    return render(request,"add_member.html",d)

def View_Member(request):
    if not request.user.is_staff:
        return redirect('login')
    member = Member.objects.all()
    d = {'member':member}
    return render(request,"view_member.html",d)

def Delete_Member(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    plan = Member.objects.get(id=pid)
    plan.delete()
    return redirect("view_member")