# formulaire/views.py (ou messagerie/views.py)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm

@login_required
def boite_reception(request):
    messages_recus = Message.objects.filter(destinataire=request.user)
    non_lus = messages_recus.filter(lu=False).count()
    
    context = {
        'messages_recus': messages_recus,
        'non_lus': non_lus,
    }
    return render(request, 'boite_reception.html', context)

@login_required
def messages_envoyes(request):
    messages_envoyes = Message.objects.filter(expediteur=request.user)
    
    return render(request, 'messages_envoyes.html', {'messages_envoyes': messages_envoyes})

@login_required
def envoyer_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.expediteur = request.user
            message.save()
            messages.success(request, 'Message envoyé avec succès!')
            return redirect('messagerie:envoyes')
    else:
        form = MessageForm()
    
    return render(request, 'envoyer_message.html', {'form': form})

@login_required
def detail_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    
    # Marquer comme lu si c'est le destinataire
    if message.destinataire == request.user and not message.lu:
        message.lu = True
        message.save()
    
    return render(request, 'detail_message.html', {'message': message})

@login_required
def supprimer_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    
    # Seul l'expéditeur ou le destinataire peut supprimer
    if message.expediteur == request.user or message.destinataire == request.user:
        message.delete()
        messages.success(request, 'Message supprimé!')
    
    return redirect('messagerie:reception')

@login_required
def marquer_comme_lu(request, message_id):
    message = get_object_or_404(Message, id=message_id, destinataire=request.user)
    message.lu = True
    message.save()
    return redirect('messagerie:reception')

@login_required
def repondre_message(request, message_id):
    message_original = get_object_or_404(Message, id=message_id)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            nouveau_message = form.save(commit=False)
            nouveau_message.expediteur = request.user
            nouveau_message.destinataire = message_original.expediteur
            nouveau_message.sujet = f"Re: {message_original.sujet}"
            nouveau_message.save()
            messages.success(request, 'Réponse envoyée!')
            return redirect('messagerie:envoyes')
    else:
        # Pré-remplir le formulaire
        initial = {
            'destinataire': message_original.expediteur,
            'sujet': f"Re: {message_original.sujet}",
        }
        form = MessageForm(initial=initial)
    
    return render(request, 'repondre.html', {
        'form': form,
        'message_original': message_original
    })