# formulaire/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['destinataire', 'sujet', 'contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control'}),
            'destinataire': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclure l'utilisateur courant de la liste des destinataires
        self.fields['destinataire'].queryset = User.objects.exclude(is_superuser=True)
        self.fields['destinataire'].label_from_instance = lambda obj: f"{obj.username} ({obj.email})"