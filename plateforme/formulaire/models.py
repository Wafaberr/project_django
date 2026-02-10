from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class AutoEntrepreneur(models.Model):
    # Choix pour le mode de prestation du service
    MODE_PRESTATION_CHOICES = [
        ('', '--- Sélectionnez ---'),
        ('presentiel', 'Présentiel'),
        ('distance', 'À distance'),
        ('en_ligne', 'En ligne'),
        ('client', 'Directement chez le client'),
        ('hybride', 'Hybride (mixte)'),
        ('projet', 'Par projet'),
        ('forfait', 'Forfait'),
    ]

    # Choix pour l'accessibilité aux personnes en situation de handicap
    HANDICAP_CHOICES = [
        ('facile', '✅ Exerçable facilement'),
        ('amenagement', '⚠️ Exerçable avec aménagements'),
        ('difficile', '⚠️ Exerçable avec difficulté'),
        ('tres_difficile', '❌ Difficulté élevée'),
    ]

    # Ajoutez ces champs qui manquent dans votre modèle
    code_activite = models.CharField(
        max_length=6,
        unique=True,
        validators=[
            MinLengthValidator(6, "Le code doit contenir au moins 6 caractères"),
            RegexValidator(
                regex='^[0-9]+$',
                message='Utilisez uniquement des chiffres',
                code='invalid_code'
            )
        ],
        help_text="Code unique de l'activité (6 chiffres)"
    )
    
    date_introduction = models.DateField(
        null=True,
        blank=True,
        help_text="Date d'introduction de l'activité"
    )
    
    # Renommez 'nom' en 'nom_activite' pour correspondre au formulaire
    nom_activite = models.CharField(
        max_length=200,
        help_text="Nom de l'activité professionnelle",
        null=True,
        blank=True,
    )
    
    # Renommez 'public_cible' en 'publics_cibles'
    publics_cibles = models.TextField(
        null=True,
        blank=True,
        help_text="Publics cibles (entreprises, particuliers, associations, etc.)"
    )
    
    # Ajoutez le champ manquant
    activites_similaires = models.TextField(
        blank=True,
        null=True,
        help_text="Activités similaires ou complémentaires"
    )
    
    # Renommez 'accessibilite_handicap' en 'capacite_handicap'
    capacite_handicap = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=HANDICAP_CHOICES
    )
    
    # Gardez les champs existants avec les bons noms
    domaine = models.CharField(max_length=100)
    sous_domaine = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Description succincte de l'activité"
    )
    objectifs = models.TextField(
        null=True,
        blank=True,
        help_text="Objectifs, tâches et missions de l'activité"
    )
    competences = models.TextField(
        null=True,
        blank=True,
        help_text="Compétences requises pour exercer l'activité"
    )
    secteurs = models.TextField(
        null=True,
        blank=True,
        help_text="Secteurs concernés par l'activité"
    )
    mode_prestation = models.CharField(
        null=True,
        blank=True,
        max_length=20,
        choices=MODE_PRESTATION_CHOICES
    )
    ressources = models.TextField(
        null=True,
        blank=True,
        help_text="Ressources, outils et équipements nécessaires"
    )
    remarques = models.TextField(
        blank=True,
        null=True,
        help_text="Remarques légales ou informations supplémentaires"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_activite} ({self.code_activite})"