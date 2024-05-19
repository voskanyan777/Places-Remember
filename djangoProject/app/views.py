from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView

from . import forms
from .models import Place, UserImage


def index(request):
    return render(request, 'index.html')


@login_required
def main_page(request):
    user_places = Place.objects.filter(user=request.user)
    image_url = UserImage.objects.filter(user=request.user).values_list('image', flat=True)[0]
    context = {
        'user_places': user_places,
        'image_url': image_url
    }
    return render(request, 'main.html', context)


def logout_user(request):
    logout(request)
    return render(request, 'index.html')


@login_required()
def add_place(request):
    # form = forms.PlaceForm()
    # return render(request, 'forms.html', {'form': form})
    if request.method == 'POST':
        form = forms.PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect('main_page')
    else:
        form = forms.PlaceForm()
    return render(request, 'forms.html', {'form': form})

