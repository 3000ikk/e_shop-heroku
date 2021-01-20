from django.core.mail import send_mail
from rest_framework import permissions


def send_activation_email(user):
    subject = 'Спасибо за регистрацию на нашем сайте'
    body = 'Спасибо за регистрацию на нашем сайте. \n'\
            'Для активации аккаунта перейдите по ссылке ниже:\n'\
            f'http://127.0.0.1:8000/v1/account/activate/{user.activation_code}/'
    
    from_email = 'e-shop@django.kg'
    recipients = [user.email]
    send_mail(
            subject=subject, message=body,
            from_email=from_email,
            recipient_list=recipients,
            fail_silently=False
            )


class IsOwnerAccount(permissions.BasePermission):
    """Permissions for check user is owner of account or superuser"""
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username or bool(request.user and request.user.is_superuser)