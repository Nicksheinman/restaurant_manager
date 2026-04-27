from django.core.mail import send_mail
import logging 
logger = logging.getLogger(__name__)
import os
import uuid
from ..models import VertificationToken

def send_email_registration(user):
    token=str(uuid.uuid4())
    VertificationToken.objects.create(user=user,token=token)
    frontend_url = os.getenv("FRONTEND_URL", "http://127.0.0.1:5173")
    confirm_link = f"{frontend_url}/email_confirm?token={token}"
    
    try:

        send_mail(
            subject='Confirm your email address',
            message=(
                f"Hi {user.username},\n\n"
                f"Thank you for registering.\n"
                f"Please confirm your email address by clicking the link below:\n\n"
                f"{confirm_link}\n\n"
                f"If you didn't create this account, you can safely ignore this email."),
            from_email='noreply@url_short.com',
            recipient_list=[user.email],
            fail_silently=False
        )

    except Exception:
        logger.exception("Email sending failed")
        raise
    