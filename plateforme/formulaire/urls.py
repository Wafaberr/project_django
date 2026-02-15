# platforms/urls.py (ou le vôtre)
from django.urls import path
from formulaire import views  # ou from . import views

app_name = 'formulaire'  # Ajoutez un namespace pour éviter les conflits de noms

urlpatterns = [
    path('editer_fiche/<int:id>/', views.modifier_fiche, name='editer_fiche'),  # NOM : 'editer_fiche'
    path('liste_fiches/', views.liste_fiches, name='liste_fiches'), 
    path('', views.home, name='home'),  # Page d'accueil de votre application
    
   
]