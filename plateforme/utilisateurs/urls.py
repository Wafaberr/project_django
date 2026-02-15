 # platforms/urls.py (ou le vôtre)
from django.urls import path
from utilisateurs import views  # ou from . import views

app_name = 'utilisateurs'  # Ajoutez un namespace pour éviter les conflits de noms

urlpatterns = [
    path('registration', views.registration_view, name='registration'),  # NOM : 'formulaire'
    path('connexion/', views.connexion_view, name='connexion'),  
    path('deconnexion/', views.deconnexion_view, name='deconnexion'),  
   
   
]