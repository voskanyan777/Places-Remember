from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Place
def index(request):
    return render(request, 'index.html')

@login_required
def main_page(request):
    user_places = Place.objects.filter(user=request.user)
    context = {'user_places': user_places}
    return render(request, 'main.html', context)

def logout_user(request):
    logout(request)
    return render(request, 'index.html')