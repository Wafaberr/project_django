from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

# Create your views here.

def registration_view(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('utilisateurs:connexion')  # Redirigez vers la page de connexion après l'inscription
    else:
        form= UserCreationForm()
    return render (request,'registration.html', {'form': form})


def connexion_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('formulaire:liste_fiches')  # Redirigez vers la liste des fiches après la connexion
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})

def deconnexion_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('utilisateurs:connexion')  # Redirigez vers la page de connexion après la déconnexion
    return HttpResponseNotAllowed(['POST'])