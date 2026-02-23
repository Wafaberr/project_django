from django.urls import path
from messagerie import views  # ou from . import views

app_name = 'messagerie'  # Ajoutez un namespace pour éviter les conflits de noms

urlpatterns = [
     path('', views.boite_reception, name='reception'),
    path('envoyes/', views.messages_envoyes, name='envoyes'),
    path('envoyer/', views.envoyer_message, name='envoyer'),
    path('message/<int:message_id>/', views.detail_message, name='detail'),
    path('message/<int:message_id>/supprimer/', views.supprimer_message, name='supprimer'),
    path('message/<int:message_id>/lu/', views.marquer_comme_lu, name='marquer_lu'),
    path('message/<int:message_id>/repondre/', views.repondre_message, name='repondre'),
    
   
]