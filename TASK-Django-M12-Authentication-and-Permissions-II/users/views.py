from django.shortcuts import redirect, render
from users.forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def register_user(req):
    form=RegistrationForm()
    if req.method=="POST":
        form=RegistrationForm(req.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            user.save()
            if user is not None:
                login(req, user)
                return redirect("home")
            else:
                return ("an 'invalid login' error message")      
    context={"form":form}
    return render(req,"register.html",context)

def logout_user(req):
    logout(req)
    return redirect("home")

def login_user(req):
    form=LoginForm()
    if req.method=="POST":
        form=LoginForm(req.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            auth_user=authenticate(username=username, password=password)
            if auth_user is not None:
                login(req,auth_user)
                return redirect("home")
    context={"form":form}
    return render(req,"login.html",context)





