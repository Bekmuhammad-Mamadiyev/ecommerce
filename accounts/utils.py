import secrets
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from core.settings.base import EMAIL_HOST

def check_otp_code(value):
    if len(str(value))!=6:
        raise ValidationError(_('The OTP code must be exactly 6 digits long.'))



def send_email(code, email):
    message = f'your code {code}'

    send_mail(
        'OTP Code',
        message,
        EMAIL_HOST,
        [email], fail_silently=False)

def generate_code():
    numbers = '123456789'
    return "".join(secrets.choice(numbers) for i in range(6))