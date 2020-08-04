from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "index.html")


def handlelogin(request):
    if request.method == "POST":
        user = request.POST.get("uname")
        passwd = request.POST.get("loginpas")
        myuser = authenticate(username=user, password=passwd)
        if myuser is not None:
            print("authenticate!")
            login(request, myuser)
            messages.success(request, "You successfully entered the world of icoder!")
            return redirect('home')
        else:
            print("no authenticate!")
            messages.error(request, "You are not authorised to enter the world of icoder")
            return redirect('home')
    return HttpResponse("login")


def handlesignup(request):
    if request.method == 'POST':
        uname = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pas = request.POST.get('pas')
        # check if email exists
        if User.objects.filter(email__exact=uname):
            messages.error(request, "Email Already Exists! Try Another Email.")
            return redirect('home')
        # create user
        user = User.objects.create_user(uname, uname, pas)
        user.email = uname
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, "You are now a member of Zakardo family")
        return redirect('home')
    else:
        return HttpResponse("There is Nothing for you here!")


def handlelogout(request):
    logout(request)
    messages.success(request, "Logout successful! Please come back to explore more!")
    return redirect('home')


def reghotel(request):
    return render(request, )


