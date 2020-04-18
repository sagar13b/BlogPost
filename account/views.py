from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from post.models import User_Details

# Create your views here.
def signup(request):
    form = UserCreationForm()
    if request.method=='POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            u = User_Details(user_link=user.instance)
            u.save()
            return redirect('sin')
        else:
            return render(request, 'signup.html',{'form':form,'error':'Username/Password cannot be accepted'})
    else:
        return render(request,'signup.html',{'form':form})

def signin(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'signin.html',{'error':'Username or password did not match'})
    else:
        return render(request, 'signin.html')

def signout(request):
    auth.logout(request)
    return redirect('home')

def user_friend(request, operation, uid):
    return redirect('home')