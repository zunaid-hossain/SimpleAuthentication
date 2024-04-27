from django.contrib import messages
from django.shortcuts import render ,redirect
from .forms import registrationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        user=registrationForm(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request ,"Registration successful")
            return redirect('login')
    
    else:
        user=registrationForm()
    
    return render(request, 'signup.html',{'user':user})


def login_user(request):

    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usernames=form.cleaned_data['username']
            pass1=form.cleaned_data['password']

            user=authenticate(username=usernames , password=pass1)
            if user is not None:
                login(request,user)
                messages.success(request,"login successful")
                return redirect('profile')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form':form})
@login_required

def profile(request):
    return render(request, 'profile.html')

@login_required
def logout_user(request):
    logout(request)
    messages.success(request,"logOut successful")
    return redirect('home')


@login_required
def Change_pass(request):
    if request.method == 'POST':
        form=PasswordChangeForm(user=request.user ,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)

    return render(request,'passChange.html',{'form':form})






@login_required
def fChange_pass(request):
    if request.method == 'POST':
        form=SetPasswordForm(user=request.user ,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form=SetPasswordForm(user=request.user)

    return render(request,'passChange.html',{'form':form})