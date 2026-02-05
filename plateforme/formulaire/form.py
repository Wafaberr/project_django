from django import forms
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils.safestring import mark_safe

class AutoEntrepreneurForm(forms.Form):
    """
    Formulaire pour la fiche d'activité d'auto-entrepreneur
    """
    
    # 01 — Code d'activité
    code_activite = forms.CharField(
        label=mark_safe('<strong>01 — Code d\'activité</strong>'),
        max_length=6,
        required=True,
        validators=[
            MinLengthValidator(6, "Le code doit contenir au moins 6 caractères"),
            RegexValidator(
                regex='^[0-9]+$',
                message='Utilisez uniquement des chiffres',
                code='invalid_code'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex:010101',
            'title': 'Code unique identifiant votre activité'
        }),
        help_text="Code unique à 6 caractères"
    )

    # 02 — Date d'introduction
    date_introduction = forms.DateField(
        label=mark_safe('<strong>02 — Date d\'introduction de l\'activité</strong>'),
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'max': '2100-12-31',
            'min': '2000-01-01'
        }),
        help_text="Date à laquelle vous avez commencé cette activité"
    )

    # 03 — Domaine
    domaine = forms.CharField(
        label=mark_safe('<strong>03 — Domaine</strong>'),
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: Informatique, Conseil, Formation...'
        }),
        help_text="Domaine principal d'activité"
    )

    # 04 — Sous-domaine
    sous_domaine = forms.CharField(
        label=mark_safe('<strong>04 — Sous-domaine</strong>'),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: Développement web, Marketing digital...'
        }),
        help_text="Spécialisation au sein du domaine"
    )

    # 05 — Nom de l'activité
    nom_activite = forms.CharField(
        label=mark_safe('<strong>05 — Nom de l\'activité</strong>'),
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: Création de sites internet'
        }),
        help_text="Nom commercial de votre activité"
    )

    # 06 — Description succincte
    description = forms.CharField(
        label=mark_safe('<strong>06 — Description succincte</strong>'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Décrivez votre activité en quelques lignes...',
            'maxlength': '500'
        }),
        help_text="Maximum 500 caractères"
    )

    # 07 — Objectifs
    objectifs = forms.CharField(
        label=mark_safe('<strong>07 — Objectifs (tâches et missions)</strong>'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Listez vos principales missions...'
        }),
        help_text="Détaillez les tâches que vous réalisez"
    )

    # 08 — Compétences requises
    competences = forms.CharField(
        label=mark_safe('<strong>08 — Compétences requises</strong>'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Ex: HTML/CSS, Python, Gestion de projet...'
        }),
        help_text="Compétences techniques et relationnelles nécessaires"
    )

    # 09 — Secteurs concernés
    SECTEURS = [
        ('industrie', 'Industrie'),
        ('energie', 'Énergie'),
        ('agriculture', 'Agriculture'),
        ('education', 'Éducation'),
        ('transport', 'Transport'),
        ('sante', 'Santé'),
        ('finance', 'Finance'),
        ('communication', 'Communication'),
        ('tourisme', 'Tourisme'),
        ('batiment', 'Bâtiment'),
        ('commerce', 'Commerce'),
        ('services', 'Services aux entreprises'),
        ('culture', 'Culture et arts'),
        ('sport', 'Sport et loisirs'),
    ]

    secteurs = forms.MultipleChoiceField(
        label=mark_safe('<strong>09 — Secteurs concernés</strong>'),
        choices=SECTEURS,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input sector-checkbox'
        }),
        help_text="Cochez tous les secteurs concernés"
    )

    # 10 — Publics cibles
    PUBLICS = [
        ('entreprises', 'Entreprises (TPE/PME)'),
        ('grandes_entreprises', 'Grandes entreprises'),
        ('organisations', 'Organisations publiques'),
        ('associations', 'Associations'),
        ('particuliers', 'Particuliers'),
        ('startups', 'Startups'),
        ('artisans', 'Artisans'),
        ('professionnels', 'Professionnels libéraux'),
    ]

    publics_cibles = forms.MultipleChoiceField(
        label=mark_safe('<strong>10 — Publics cibles</strong>'),
        choices=PUBLICS,
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input public-checkbox'
        }),
        help_text="Sélectionnez vos clients types"
    )

    # 11 — Mode de prestation
    MODE_PRESTATION = [
        ('', '--- Sélectionnez ---'),
        ('presentiel', 'Présentiel'),
        ('distance', 'À distance'),
        ('en_ligne', 'En ligne'),
        ('client', 'Directement chez le client'),
        ('hybride', 'Hybride (mixte)'),
        ('projet', 'Par projet'),
        ('forfait', 'Forfait'),
    ]

    mode_prestation = forms.ChoiceField(
        label=mark_safe('<strong>11 — Mode de prestation de service</strong>'),
        choices=MODE_PRESTATION,
        widget=forms.Select(attrs={
            'class': 'form-select'
        }),
        help_text="Comment fournissez-vous vos services ?"
    )

    # 12 — Ressources et outils
    ressources = forms.CharField(
        label=mark_safe('<strong>12 — Ressources et outils nécessaires</strong>'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Ex: Ordinateur, logiciels, véhicule, local...'
        }),
        required=False,
        help_text="Équipements nécessaires pour exercer"
    )

    # 13 — Activités similaires
    activites_similaires = forms.CharField(
        label=mark_safe('<strong>13 — Activités similaires ou complémentaires</strong>'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Activités que vous pourriez proposer...'
        }),
        required=False,
        help_text="Services connexes possibles"
    )

    # 14 — Capacité handicap
    HANDICAP = [
        ('facile', '✅ Exerçable facilement'),
        ('amenagement', '⚠️ Exerçable avec aménagements'),
        ('difficile', '⚠️ Exerçable avec difficulté'),
        ('tres_difficile', '❌ Difficulté élevée'),
    ]

    capacite_handicap = forms.ChoiceField(
        label=mark_safe('<strong>14 — Capacité des personnes en situation de handicap</strong>'),
        choices=HANDICAP,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input handicap-radio'
        }),
        help_text="Accessibilité de votre activité"
    )

    # 15 — Remarques supplémentaires
    remarques = forms.CharField(
        label=mark_safe('<strong>15 — Remarques supplémentaires</strong>'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Informations complémentaires...'
        }),
        required=False,
        help_text="Toute information utile non couverte précédemment"
    )

    
    def clean_date_introduction(self):
        """Validation de la date"""
        date = self.cleaned_data.get('date_introduction')
        
        # Empêcher les dates futures (optionnel)
        # from datetime import date
        # if date and date > date.today():
        #     raise forms.ValidationError("La date ne peut pas être dans le futur")
        
        return date

    def clean(self):
        """Validation globale du formulaire"""
        cleaned_data = super().clean()
        
        # Exemple de validation croisée
        domaine = cleaned_data.get('domaine')
        sous_domaine = cleaned_data.get('sous_domaine')
        
        if sous_domaine and domaine and sous_domaine.lower() == domaine.lower():
            self.add_error(
                'sous_domaine',
                "Le sous-domaine doit être différent du domaine principal"
            )
        
        # Vérifier qu'au moins un secteur est sélectionné
        secteurs = cleaned_data.get('secteurs')
        if not secteurs or len(secteurs) == 0:
            self.add_error(
                'secteurs',
                "Veuillez sélectionner au moins un secteur"
            )
        
        return cleaned_data

    # Configuration des erreurs
    error_messages = {
        'required': 'Ce champ est obligatoire',
        'invalid': 'Veuillez saisir une valeur valide',
        'max_length': 'La valeur est trop longue (maximum %(limit_value)d caractères)',
    }

    def __init__(self, *args, **kwargs):
        """Initialisation avec personnalisations supplémentaires"""
        super().__init__(*args, **kwargs)
        
        # Ajouter des classes CSS aux champs requis
        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') 
        
        # Personnalisation spécifique
        self.fields['description'].widget.attrs['data-counter'] = '500'
        self.fields['date_introduction'].widget.attrs['onchange'] = 'validateDate(this)'