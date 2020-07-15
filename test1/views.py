from django.shortcuts import render,redirect
from .forms import Detailsform
from .models import Details  
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='users:login')
def add(request):  
    if request.method == "POST":  
        form = Detailsform(request.POST)  
        if form.is_valid():
            newform=form.save(commit=False)
            newform.owner=request.user
            newform.save()
            return redirect('/')  
             
    else:  
        form = Detailsform()  
    return render(request,"add.html",{'form':form})  


def show(request):  
    employees = Details.objects.all()  
    return render(request,"home.html",{'employees':employees})  

def entry(request):
    return render(request,"add.html")


    