from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
from .forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


@login_required
def show_profile(request) :
    return render(request, 'show_profile.html')

def signup_complete(request) :
    return render(request, 'signup_complete.html')

def profile_info(request) :
    return render(request, 'profile_info.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('signup_complete')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def signup(request) :
    if request.method == 'POST' :
        if request.POST['password1'] == request.POST['password2'] :
            try :
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error' : '이미 존재하는 아이디입니다.'})
            except User.DoesNotExist :
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('profile')
        else :
            return render(request, 'signup.html', {'error':'Passwords must match'})
    else :
        return render(request, 'signup.html')



def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect('home')
        else :
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

@login_required
def logout(request) :
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')
