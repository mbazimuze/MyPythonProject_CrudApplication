from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# create your views here
def home(request):
    return render(request,"Authentication/index.html")

def signup(request):

    if request.method == "POST":

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
           messages.error(request,"Username already exists")
           return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"Email already registered")
            return redirect('home')

        if len(username)>15:
            messages.error(request,"Username must be less that 20 characters")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request,"Invalid password")
            return redirect('home')

        if not pass1.isalnum():
            messages.error(request, "Password must be alphanumeric")
            return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your account has been created")

        return redirect('signin')

    return render(request,"Authentication/signup.html")

def signin(request):

    if request.method == "POST":
       username = request.POST['username']
       pass1 = request.POST['pass1']

       user = authenticate(username=username, password=pass1)
       if user is not None:
           login(request,user)
           fname = user.first_name
           return render(request,'Authentication/index.html',{'fname': fname})
       else:
           messages.error(request,"Bad credentials")
           return redirect('home')

    return render(request,"Authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"You're successfully logged out")
    return redirect('home')

