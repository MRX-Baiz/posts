from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateForm, ProfileUpdate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger('users')

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
    logger.debug("HIT users.profile view")
    if request.method == 'POST':
        logger.debug(f"=== PROFILE UPDATE START for user={request.user.username} ===")
        logger.debug(f"POST data: {request.POST}")
        logger.debug(f"FILES received: {request.FILES}")
        
        update_form = UpdateForm(request.POST or None, instance=request.user)
        profile_form = ProfileUpdate(request.POST or None, request.FILES or None, instance=request.user.profilemodel)

        if update_form.is_valid() and profile_form.is_valid():
            logger.debug("Forms are valid, saving...")
            update_form.save()
            profile_form.save()
            
            # Log saved profile data
            profile = request.user.profilemodel
            logger.debug(f"✓ Profile saved successfully")
            logger.debug(f"  - Image name: {profile.image.name}")
            logger.debug(f"  - Image URL: {profile.image.url}")
            logger.debug(f"  - Profile: {profile}")
            logger.debug(f"=== PROFILE UPDATE END ===")
            
            from django.contrib import messages
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile-page')
        else:
            logger.warning(f"Form validation failed: update_form.errors={update_form.errors}, profile_form.errors={profile_form.errors}")
    else:
        update_form = UpdateForm(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user.profilemodel)

    context = {
        'update_form': update_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile.html', context)


