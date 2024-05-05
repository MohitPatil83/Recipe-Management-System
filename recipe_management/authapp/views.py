from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login,authenticate
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.method=="POST":
        #fetch form data
        uname=request.POST['uname']
        upass=request.POST['upass']
        #validate
        context={}
        if uname=='' or upass=='':
            context['errmsg']="Field cannot be Blank"
            return render(request,'authapp/login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            if u is not None:
                login(request,u)
                return redirect('/')
            else:
                context['errmsg']="Invalid User name and Passward"
                return render(request,'authapp/login.html',context)

    else:
        return render(request,'authapp/login.html')

def user_register(request):
    if request.method=="POST":
        #fectch data from form
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        uemail=request.POST['uemail']
        #print("Username:",uname)
        #print("Passward:",upass)
        #print("Confirm Passward:",ucpass)
        #print("Email:",uemail)

        #validation
        context={}
        if uname=='' or upass=='' or ucpass=='' or uemail=='':
            context['errmsg']="Field cannot be empty"
            return render(request,'authapp/register.html',context)
        
        elif upass!=ucpass:
            context['errmsg']="Passward and confirm passward didn't match"
            return render(request,'authapp/register.html',context)
        
        else:
            u=User.objects.create(username=uname,email=uemail)
            u.set_password(upass)
            u.save()

            context['success']="User Created Successfully,Please Login"
            return render(request,'authapp/register.html',context)
          

    else:
        return render(request,'authapp/register.html')  


def user_logout(request):
    logout(request)
    return redirect('authapp/login')