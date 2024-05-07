from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import login,authenticate,logout

# Create your views here.


def register(request):
    form=UserForm()
    context={
        "form": form
    }
    if request.method == 'POST':
        form=UserForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect("login")

    return render(request,'register.html',context)


def userLogin(request):

    if request.method == 'POST':
        username= request.POST["username"]
        userpass= request.POST["userpass"]

        user = authenticate(request,username=username,password=userpass)

        if user is not None:
            login(request,user)
            return redirect("browse")

    return render(request,'login.html')


def browse(request):

    profiller = Profiles.objects.filter(owner=request.user)
    context={
        "profiller":profiller
    }

    return render(request,"browse.html",context)


def createProfil(request):
    form = ProfileForm()
    context = {
        "form":form
    }

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.owner = request.user
            profil.save()
            return redirect("browse")

    return render(request,"create-profil.html",context)

def hesap(request):
    return render(request,"hesap.html")

def userLogout(request):
    logout(request)
    return redirect("index")

def removeAccount(request):
    user=request.user
    user.delete()
    return redirect("index")