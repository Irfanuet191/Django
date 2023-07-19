from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['confirm_password']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("User name taken")
                messages.info(request,"User name taken")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                print("Email taken")
                messages.info(request,"Email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password1)
                user.save()
                print("User created")
                return redirect('/')
        else:
            print("passwor missmatch")
            messages.info(request,"passwor missmatch")
            return redirect('register')
        
    else:
        return render(request,"registration.html")