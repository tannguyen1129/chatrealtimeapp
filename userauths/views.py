from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

from userauths.forms import UserRegisterForm, profileUpdateForm ,userUpdateForm
from userauths.models import Profile, Follow

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # Profile.get_or_create(user=request.user)
            username = form.cleaned_data.get('email')

            messages.success(request, f'Hurray your account was created!!')
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],)
            login(request, new_user)
            return redirect('chats:message')
            


    elif request.user.is_authenticated:
        return redirect('base:index')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'userauths/sign-up.html', context)

def profile(request, username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)
        my_studee_course = profile.favourite_course.all()
        follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

        context = {
        'user':user,
        'profile':profile,

    }
    else:
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)
        
        followers_count = Follow.objects.filter(following=user).count()

        
        context = {
            'profile': profile,
        }
    return render(request, 'userauths/profile.html', context)



@login_required
def profileUpdate(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        p_form = profileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = userUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            return redirect('chats:message')
    else:
        p_form = profileUpdateForm(instance=request.user.profile)
        u_form = userUpdateForm(instance=request.user)
    
    context = {
        'p_form': p_form,
        'u_form': u_form,
    }
    return render(request, 'userauths/profile-update.html', context)


@login_required
def follow(request, username, option):
    user = request.user.username
    following = get_object_or_404(User, username=username)

    try:
        f, created = Follow.objects.get_or_create(follower=request.user, following=following)

        if int(option) == 0:
            f.delete()
        else:
            pass
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    except User.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def error404View(request):
    return render(request, 'base/404.html')

