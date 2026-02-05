# platforms/urls.py (ou le vôtre)
from django.urls import path
from formulaire import views  # ou from . import views

urlpatterns = [
    path('', views.formulaire_view, name='formulaire'),  # NOM : 'formulaire'
    path('confirmation/', views.confirmation, name='confirmation'),
]