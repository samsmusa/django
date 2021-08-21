from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import CustomUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def sign_Up(request):
    form = CustomUser()
    if request.method == "POST":
        form = CustomUser(request.POST)
        if form.is_valid():
            form.save()
            login(request, form)
            
            redirect("quizes:main-view")
        
    context = {
        "form":form
    }
    return render(request, "users/signup.html", context)


login_required(login_url="users:login")
def logoutPage(request):
    logout(request)

    return redirect('users:login')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('users:account')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('quizes:main-view')
        
    return render(request, 'users/login.html', )

