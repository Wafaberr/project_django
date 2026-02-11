from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .form import AutoEntrepreneurForm
from .models import AutoEntrepreneur
# Create your views here.


# formulaire/views.py
def modifier_fiche(request, id):
    fiche = get_object_or_404(AutoEntrepreneur, id=id)
    
    if request.method == "POST":
        form = AutoEntrepreneurForm(request.POST)
        
        # Le formulaire sera toujours valide car aucun champ n'est requis
        if form.is_valid():
            data = form.cleaned_data
            
            # Utilisez get() avec valeur par défaut
            fiche.code_activite = data.get('code_activite') or ''
            fiche.date_introduction = data.get('date_introduction')
            fiche.domaine = data.get('domaine') or ''
            fiche.sous_domaine = data.get('sous_domaine') or ''
            fiche.nom_activite = data.get('nom_activite') or ''
            fiche.description = data.get('description') or ''
            fiche.objectifs = data.get('objectifs') or ''
            fiche.competences = data.get('competences') or ''
            
            # Pour les listes
            secteurs = data.get('secteurs', [])
            fiche.secteurs = ','.join(secteurs) if secteurs else ''
            
            publics_cibles = data.get('publics_cibles', [])
            fiche.publics_cibles = ','.join(publics_cibles) if publics_cibles else ''
            
            fiche.mode_prestation = data.get('mode_prestation') or ''
            fiche.ressources = data.get('ressources') or ''
            fiche.activites_similaires = data.get('activites_similaires') or ''
            fiche.capacite_handicap = data.get('capacite_handicap') or ''
            fiche.remarques = data.get('remarques') or ''
            
            fiche.save()
            fiches = AutoEntrepreneur.objects.all()  # Récupérer toutes les fiches après modification
            return render(request, 'liste_fiches.html', {'fiches': fiches}) # Redirigez vers la liste des fiches après la modification
    
    else:
        # Mode GET
        initial_data = {
            'code_activite': fiche.code_activite or '',
            'date_introduction': fiche.date_introduction,
            'domaine': fiche.domaine or '',
            'sous_domaine': fiche.sous_domaine or '',
            'nom_activite': fiche.nom_activite or '',
            'description': fiche.description or '',
            'objectifs': fiche.objectifs or '',
            'competences': fiche.competences or '',
            'secteurs': fiche.secteurs.split(',') if fiche.secteurs else [],
            'publics_cibles': fiche.publics_cibles.split(',') if fiche.publics_cibles else [],
            'mode_prestation': fiche.mode_prestation or '',
            'ressources': fiche.ressources or '',
            'activites_similaires': fiche.activites_similaires or '',
            'capacite_handicap': fiche.capacite_handicap or '',
            'remarques': fiche.remarques or '',
        }
        
        form = AutoEntrepreneurForm(initial=initial_data)
    
    return render(request, 'fiche.html', {
        'form': form,
        'fiche': fiche,
        'edition_mode': True
    })

def liste_fiches(request):
    fiches = AutoEntrepreneur.objects.all()  # Récupérer toutes les fiches

    sort_by = request.GET.get('sort', 'code_activite')  # Par défaut tri par code_activite
    order = request.GET.get('order', 'asc')  # Par défaut ascendant
    
    # Construire le champ de tri
    if order == 'desc':
        sort_by = f'-{sort_by}'  # Ajoute le signe - pour descendant
    
    # Récupérer et trier les fiches
    fiches = AutoEntrepreneur.objects.all().order_by(sort_by)
    
    # Passer les paramètres actuels au template
    context = {
        'fiches': fiches,
        'current_sort': request.GET.get('sort', 'code_activite'),
        'current_order': order,}
    return render(request, 'liste_fiches.html', context)
