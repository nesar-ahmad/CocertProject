from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileEditForm, RegisterForm, UserEditForm
from django.contrib import messages
from django.contrib.auth.models import User


def loginView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # user is authenticated
            login(request, user)
            if request.GET.get("next"):
                # after login, go to the page that requested from the url.
                return HttpResponseRedirect(request.GET.get("next"))
            else:
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                'username': username,
                'error_message': 'اطلاعات کاربری شما درست نمی باشد.'}
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html')


def logoutView(request):
    logout(request)
    return render(request, 'accounts/log_out.html')


@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    """Edit an existing Profile."""
    if request.method != 'POST':
        # Initial request; pre-fill form with the current profile.
        profiel_edit_form = ProfileEditForm(instance=request.user.profile)
        user_edit_form = UserEditForm(instance=request.user)
    else:
        # POST data submitted; process data.
        profiel_edit_form = ProfileEditForm(
            request.POST, request.FILES, instance=request.user.profile)
        user_edit_form = UserEditForm(request.POST, instance=request.user)
        if profiel_edit_form.is_valid() and user_edit_form.is_valid():
            profiel_edit_form.save()
            user_edit_form.save()
            # messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect(reverse('accounts:profile'))
        else:
            messages.error(request, 'Error updating your profile')

    context = {'profiel_edit_form': profiel_edit_form,
                'profile_edit_img': request.user.profile.image,
                'user_edit_form': user_edit_form}
    return render(request, 'accounts/edit_profile.html', context)


def register(request):
    # Registeration for User and Profile
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            user.save()

            profile = Profile(
                user=user,
                gender=form.cleaned_data["gender"],
                credit=form.cleaned_data["credit"],
                image=form.cleaned_data["image"]
            )
            profile.save()
        return render(request, 'accounts/register_done.html', {'user': user})
    else:
        form = RegisterForm()
    context = {'form': form}

    return render(request, 'accounts/register.html', context)
