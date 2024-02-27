from django.shortcuts import render,HttpResponse,redirect
from .models import hlo
# Create your views here.
def home(request):
    return render(request,"home.html")

def lol(request):
    return HttpResponse("hlo")

def db(request):
   if request.method=="POST":
       username=request.POST['username']
       password=request.POST['password'] 

       h=hlo()
       h.username=username
       h.password=password
       h.save()
       return redirect("h/t")
   else:
       return HttpResponse("didnt work")

def fet(request):
    obj=hlo.objects.all()
    return render(request,'index.html',{"obj":obj})