from django.core.mail import send_mail
from django.conf import settings
import random
from .models import User


def send_otp_via_email(email):
    subject = "Your account varification email"
    otp = "".join([str(random.randint(0, 1000000) % 10) for _ in range(6)])
    massage = f'Assalamu alaykum Thanks for using our library site /n Kitoblar Olami - {otp} is your verification code'
    email_from = settings.EMAIL_HOST
    send_mail(subject, massage, email_from, [email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
