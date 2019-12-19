from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .script import get_anime_info
from .models import AnimeInfo


def home(request):
    following_dict = {
        "following_ld_list": [],
        "following_sd_list": [],
        "following_hd_list": [],
        "following_fhd_list": [],
    }
    if request.user.is_authenticated:

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
    else:
        pass
    return render(request, 'main/home.html', {"ai": AnimeInfo.objects.all(),"following":following_dict})

def airing(request):
    following_dict = {
        "following_ld_list": [],
        "following_sd_list": [],
        "following_hd_list": [],
        "following_fhd_list": [],
    }
    if request.user.is_authenticated:

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
    else:
        pass
    return render(request, 'main/airing.html', {"ai": AnimeInfo.objects.all(), "following":following_dict})

def following_ld(request):
    if request.method =="POST":
        id = request.POST.get('id')
        anime = get_object_or_404(AnimeInfo, id=id)
        if anime.following_ld.filter(id = request.user.id).exists():
            anime.following_ld.remove(request.user)
        else:
            anime.following_ld.add(request.user)
    return HttpResponse("ok")

def following_sd(request):
    if request.method =="POST":
        id = request.POST.get('id')
        anime = get_object_or_404(AnimeInfo, id=id)
        if anime.following_sd.filter(id = request.user.id).exists():
            anime.following_sd.remove(request.user)
        else:
            anime.following_sd.add(request.user)
    return HttpResponse("ok")

def following_hd(request):
    if request.method =="POST":
        id = request.POST.get('id')
        anime = get_object_or_404(AnimeInfo, id=id)
        if anime.following_hd.filter(id = request.user.id).exists():
            anime.following_hd.remove(request.user)
        else:
            anime.following_hd.add(request.user)
    return HttpResponse("ok")

def following_fhd(request):
    if request.method =="POST":
        id = request.POST.get('id')
        anime = get_object_or_404(AnimeInfo, id=id)
        if anime.following_fhd.filter(id = request.user.id).exists():
            anime.following_fhd.remove(request.user)
        else:
            anime.following_fhd.add(request.user)
    return HttpResponse("ok")

class SearchListView(ListView):

    template_name = 'main/search.html'
    context_object_name = 'ai'

    def get(self, request, *args, **kwargs):
        self.search_term = request.GET.get('search')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return AnimeInfo.objects.filter(title__icontains = self.search_term )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        following_dict = {
            "following_ld_list": [],
            "following_sd_list": [],
            "following_hd_list": [],
            "following_fhd_list": [],
        }
        if self.request.user.is_authenticated:

            for anime in AnimeInfo.objects.all():
                if anime.following_ld.filter(id = self.request.user.id).exists():
                    following_dict["following_ld_list"].append(anime.id)
                if anime.following_sd.filter(id = self.request.user.id).exists():
                    following_dict["following_sd_list"].append(anime.id)
                if anime.following_hd.filter(id = self.request.user.id).exists():
                    following_dict["following_hd_list"].append(anime.id)
                if anime.following_fhd.filter(id = self.request.user.id).exists():
                    following_dict["following_fhd_list"].append(anime.id)
                else:
                    pass
        else:
            pass
        context["following"] = following_dict
        return context
