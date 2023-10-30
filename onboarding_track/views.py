from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from rest_framework import viewsets
from .serializers import EmployeeSerializer,EmployeeAllSerializer
from django.views.generic import  DetailView
from rest_framework import generics,status
from django.contrib import messages
from .models import Employee
from .forms import AddRecordForm


def home(request):
    reocrds=Employee.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,"You have successfully Logged in!")
            return redirect('home')
        else:
            messages.success(request,"There's some error while you are trying to login..")
            return redirect('home')
    else:
        return render(request,'home.html',{})
    
    
    
def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Record added successfully...")
                return redirect('home')
            


        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to do that..")
        return redirect('home')  
    
def show_reocrd(request):
    
    records=Employee.objects.all()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,"You are logged in hence you can view the details!")
            return redirect('home')
        else:
            messages.success(request,"There's some error while you are trying to login..")
            return redirect('home')
    else:
        return render(request,'all_records.html',{'records':records})
    
def Employee_record(request, pk):
    if request.user.is_authenticated:
        #Lookup record

        Employee_record=Employee.objects.get(id=pk)
        return render(request,'record.html' ,{'Employee_record':Employee_record})
    
    else:
        messages.success(request,"You must be logged in to get the records!")
        return redirect('home')
          


def logout_user(request):
    logout(request)
    messages.success(request,"You have logged out!!")
    return redirect('home')


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer
    
    
def mark_onboarded(request, pk):
    if request.user.is_authenticated:
        #Lookup record

        Employee_record=Employee.objects.get(id=pk)
        if not Employee_record.is_onboarded:
            Employee_record.is_onboarded=True
            Employee_record.save()
            
            
        return render(request,'record.html' ,{'Employee_record':Employee_record})
    
    else:
        messages.success(request,"You must be logged in to get the records!")
        return redirect('home')



def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it=Employee.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,f"The record of Employee {delete_it.first_name} {delete_it.last_name}  has been successfully deleted!")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in to do that..")
        return redirect('home')


    
    
    
    


    
    
    



        


# Create your views here.
