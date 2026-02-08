from django.http import HttpResponse
from django.shortcuts import redirect, render
from .form import AutoEntrepreneurForm
from .models import AutoEntrepreneur
# Create your views here.


def formulaire_view(request):
    if request.method == 'POST':
        form = AutoEntrepreneurForm(request.POST)
        if form.is_valid():
            # Traitez les données du formulaire et enregistrez-les en base
            data = form.cleaned_data

            # Mapper les champs du formulaire aux champs du modèle
            ae = AutoEntrepreneur.objects.create(
                code=data.get('code_activite'),
                domaine=data.get('domaine'),
                sous_domaine=data.get('sous_domaine') or '',
                nom=data.get('nom_activite'),
                description=data.get('description'),
                objectifs=data.get('objectifs'),
                competences=data.get('competences'),
                secteurs=','.join(data.get('secteurs', [])),
                public_cible=','.join(data.get('publics_cibles', [])),
                mode_prestation=data.get('mode_prestation') or '',
                teletravail=data.get('teletravail', 'non'),
                ressources=data.get('ressources', '') or '',
                accessibilite_handicap=data.get('capacite_handicap') or '',
                remarques=data.get('remarques', '') or '',
            )

            return render(request, 'formulaire/confirmation.html')  # Redirigez vers une page de succès
    else:
        form = AutoEntrepreneurForm()

    return render(request, 'formulaire/form.html', {'form': form})

def confirmation(request):
    return render(request, 'confirmation.html')


