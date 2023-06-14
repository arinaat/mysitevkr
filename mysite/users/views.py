from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from gallery.models import Post, Images
from .models import User
from django.views import View
from django.http import HttpResponse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("home")

    else:
        form = UserLoginForm()
    context['login_form'] = form
    return render(request, 'users/login.html', context)

def registration_view(request):
    context = {}
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = UserRegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    context = {}
    user = User.objects.get(email=request.user.email)
    posts = Post.objects.filter(user=user.id)
    # id__in = posts.id
    images = Images.objects.all()
    # images = Images.objects.filter(id__in = posts)
    if request.POST:
        form = UserProfileForm(data=request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=user)
    context['profile'] = form
    context['img'] = user.image.url
    context['posts'] = posts
    context['images'] = images
    return render(request, 'users/profile.html', context)
