from django.http import HttpResponse
from django.shortcuts import redirect, render
from .form import AutoEntrepreneurForm
from .models import AutoEntrepreneur
# Create your views here.


def formulaire_view(request):
    if request.method == 'POST':
        fiche = AutoEntrepreneurForm(request.POST)
        if fiche.is_valid():
            # Traitez les données du formulaire et enregistrez-les en base
            data = fiche.cleaned_data

            # # Mapper les champs du formulaire aux champs du modèle
            # ae = AutoEntrepreneur.objects.create(
            #     code=data.get('code_activite'),
            #     domaine=data.get('domaine'),
            #     sous_domaine=data.get('sous_domaine') or '',
            #     nom=data.get('nom_activite'),
            #     description=data.get('description'),
            #     objectifs=data.get('objectifs'),
            #     competences=data.get('competences'),
            #     secteurs=','.join(data.get('secteurs', [])),
            #     public_cible=','.join(data.get('publics_cibles', [])),
            #     mode_prestation=data.get('mode_prestation') or '',
            #     teletravail=data.get('teletravail', 'non'),
            #     ressources=data.get('ressources', '') or '',
            #     accessibilite_handicap=data.get('capacite_handicap') or '',
            #     remarques=data.get('remarques', '') or '',
            # )

            return render(request, 'liste_fiches.html')  # Redirigez vers une page de succès
    else:
        fiche = AutoEntrepreneurForm()

    return render(request, 'fiches.html', {'fiche': fiche})

def liste_fiches(request):
    fiches = AutoEntrepreneur.objects.all()  # Récupérer toutes les fiches
    return render(request, 'liste_fiches.html', {'fiches': fiches})


