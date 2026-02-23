from .models import Message

def messages_non_lus(request):
    if request.user.is_authenticated:
        non_lus = Message.objects.filter(
            destinataire=request.user,
            lu=False
        ).count()
    else:
        non_lus = 0

    return {
        "non_lus": non_lus
    }
