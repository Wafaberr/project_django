from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def registration_view(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('formulaire:liste_fiches')  # Redirigez vers la page d'accueil ou une autre page après l'inscription
    else:
        form= UserCreationForm()
    return render (request,'registration.html', {'form': form})
