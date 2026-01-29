from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    
    else:
        initial_data = {'username':'', 'password':'', 'confirm_password':''}
        form = UserCreationForm(initial=initial_data)
        return render(request, 'register.html',{'form':form})


def login_view(request):
        if request.method == 'POST':
            form = AuthenticationForm(request.POST)
            if form.is_valid:
                user = form.get_user()
                login(request,user)
                return redirect('dashboard')
    
        else:
            initial_data = {'username':'', 'password':'', 'confirm_password':''}
            form = AuthenticationForm(initial=initial_data)
            return render(request, 'login.html',{'form':form})

    

def logout_view(request):
    logout(request)
    return redirect('login') #redirecting to the login page

def dashboard_view(request):
    return redirect(request, 'dashboard.html') 


# def app(request):
#     return render(request, 'app.html')
