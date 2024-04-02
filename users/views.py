from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateForm, ProfileUpdate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form = SignUpForm()

    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('login_page')


@login_required
def profile(request):
    if request.method == 'POST':
        update_form = UpdateForm(request.POST or None, instance=request.user)
        profile_form = ProfileUpdate(request.POST or None, request.FILES or None, instance=request.user.profilemodel)

        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            return redirect('profile-page')
    else:
        update_form = UpdateForm(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user.profilemodel)

    context = {
        'update_form': update_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile.html', context)


