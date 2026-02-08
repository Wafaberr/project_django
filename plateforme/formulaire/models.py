from django.db import models

class AutoEntrepreneur(models.Model):
 # Choix pour le mode de prestation du service
    MODE_PRESTATION_CHOICES = [
        ('en_ligne', 'En ligne'),
        ('chez_client', 'Chez le client'),
        ('hybride', 'Hybride'),
    ]

    # Choix pour la possibilité de travail à distance
    TELETRAVAIL_CHOICES = [
        ('total', 'Totalement'),
        ('partiel', 'Partiellement'),
        ('non', 'Non réalisable'),
    ]

    # Choix pour l'accessibilité aux personnes en situation de handicap
    HANDICAP_CHOICES = [
        ('facile', 'Exerçable facilement'),
        ('amenagement', 'Exerçable avec aménagements'),
        ('difficile', 'Exerçable avec difficulté'),
        ('tres_difficile', 'Difficulté élevée à exercer'),
    ]

    # Informations générales
    code = models.CharField(
        max_length=50,
        unique=True,
        help_text="Code unique de l'activité"
    )
    domaine = models.CharField(max_length=100)
    sous_domaine = models.CharField(max_length=100)
    nom = models.CharField(
        max_length=200,
        help_text="Nom de l'activité professionnelle"
    )

    # Description et contenu
    description = models.TextField(
        help_text="Description succincte de l'activité"
    )
    objectifs = models.TextField(
        help_text="Objectifs, tâches et missions de l'activité"
    )
    competences = models.TextField(
        help_text="Compétences requises pour exercer l'activité"
    )
    secteurs = models.TextField(
        help_text="Secteurs concernés par l'activité"
    )
    public_cible = models.TextField(
        help_text="Publics cibles (entreprises, particuliers, associations, etc.)"
    )

    # Modalités d'exercice
    mode_prestation = models.CharField(
        max_length=20,
        choices=MODE_PRESTATION_CHOICES
    )

    teletravail = models.CharField(
        max_length=20,
        choices=TELETRAVAIL_CHOICES
    )

    # Ressources et accessibilité
    ressources = models.TextField(
        help_text="Ressources, outils et équipements nécessaires"
    )

    accessibilite_handicap = models.CharField(
        max_length=20,
        choices=HANDICAP_CHOICES
    )

    # Remarques complémentaires
    remarques = models.TextField(
        blank=True,
        null=True,
        help_text="Remarques légales ou informations supplémentaires"
    )

    # Date de création de la fiche
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Ce qui s'affiche dans l'admin Django
        return self.nom