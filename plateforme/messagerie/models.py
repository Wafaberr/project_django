
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Message(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_envoyes')
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_recus')
    sujet = models.CharField(max_length=200)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(default=timezone.now)
    lu = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_envoi']
    
    def __str__(self):
        return f"{self.sujet} - de {self.expediteur} à {self.destinataire}"