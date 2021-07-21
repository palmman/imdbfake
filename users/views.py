from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

@login_required(login_url='login')
def profiles(request):

    profile = request.user.profile

    context = {
        'profile': profile,
    }

    return render(request, 'users/profiles.html', context)

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome.')
            return redirect('home')
        else:
            messages.error(request, 'Usernamr or Password is incorrect.')

    context = {

    }

    return render(request, 'login.html', context)

def register(request):

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('home')
        else:
            pass

    context = {
        'form':form,
    }

    return render(request, 'register.html', context)

def logoutPage(request):

    logout(request)
    messages.success(request, 'You are logged out.')

    return redirect('home')

@login_required(login_url='login')
def editProfile(request):

    profile = request.user.profile

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()

            return redirect('profiles')


    context = {
        'form':form,
    }

    return render(request, 'users/edit_profile.html', context)
