from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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

            return redirect('formulaire:liste_fiches')  # Redirigez vers la liste des fiches après la connexion
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})
           