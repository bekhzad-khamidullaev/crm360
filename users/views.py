from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')

        else:
            return render(request, 'index.html')

    else:
        return render(request, 'index.html')

def login_user(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    # messages.success(request, "Successfully logged out!")
    return redirect('index')