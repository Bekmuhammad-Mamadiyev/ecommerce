from datetime import datetime, timedelta

from django.db.models.signals import post_save

from django.dispatch import receiver

from accounts.models import User, VerificationOtp
from accounts.utils import generate_code
from core.settings.base import OTP_CODE_ACTIVATION_TIME
from accounts.utils import send_email

@receiver(post_save, sender=User)
def create_verification_otp(sender, instance, created, **kwargs):
    if created:
        code = generate_code()
        VerificationOtp.objects.create(user=instance, type=VerificationOtp.VerificationType.REGISTER,
                                       code=code,
                                       expires_in=datetime.now() + timedelta(minutes=OTP_CODE_ACTIVATION_TIME))
        send_email(code=code, email=instance.email)
        print('signal is working')
