from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Place
def index(request):
    return render(request, 'index.html')

@login_required
def main_page(request):
    user_places = Place.objects.filter(user=request.user)
    context = {'user_places': user_places}
    return render(request, 'main.html', context)