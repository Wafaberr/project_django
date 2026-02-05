from django.shortcuts import render
from .form import AutoEntrepreneurForm
# Create your views here.


def formulaire_view(request):
    if request.method == 'POST':
        form = AutoEntrepreneurForm(request.POST)
        if form.is_valid():
            # Traitez les données du formulaire ici (par exemple, en les enregistrant dans la base de données)
            # Vous pouvez accéder aux données du formulaire avec form.cleaned_data
            return render(request, 'formulaire/confirmation.html')  # Redirigez vers une page de succès
    else:
        form = AutoEntrepreneurForm()

    return render(request, 'formulaire/form.html', {'form': form})

def confirmation(request):
    return render(request, 'confirmation.html')