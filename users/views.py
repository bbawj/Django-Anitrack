from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import UserRegisterForm, UserUpdateForm
from main.models import AnimeInfo


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! Please login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    id_list = []

    ld_list = AnimeInfo.objects.filter(following_ld = request.user.id)
    sd_list = AnimeInfo.objects.filter(following_sd = request.user.id)
    hd_list = AnimeInfo.objects.filter(following_hd = request.user.id)
    fhd_list = AnimeInfo.objects.filter(following_fhd = request.user.id)

    for item in ld_list:
        id_list.append(item.id)
    for item in sd_list:
        id_list.append(item.id)
    for item in hd_list:
        id_list.append(item.id)
    for item in fhd_list:
        id_list.append(item.id)

    id_list = set(id_list)
    anime_dict = AnimeInfo.objects.in_bulk(id_list, field_name= 'id')
    anime_list = list(anime_dict.values())
    following_dict = {
        "following_ld_list": [],
        "following_sd_list": [],
        "following_hd_list": [],
        "following_fhd_list": [],
    }

    for anime in AnimeInfo.objects.all():
        if anime.following_ld.filter(id = request.user.id).exists():
            following_dict["following_ld_list"].append(anime.id)
        if anime.following_sd.filter(id = request.user.id).exists():
            following_dict["following_sd_list"].append(anime.id)
        if anime.following_hd.filter(id = request.user.id).exists():
            following_dict["following_hd_list"].append(anime.id)
        if anime.following_fhd.filter(id = request.user.id).exists():
            following_dict["following_fhd_list"].append(anime.id)
        else:
            pass

    context = {
     'u_form':u_form,
     'anime': anime_list,
     'following': following_dict
    }
    return render(request, 'users/profile.html',context)
