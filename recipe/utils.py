from .models import EmailQueue

def queue_email(user, subject, message):
    EmailQueue.objects.create(user=user, subject=subject, message=message)
