from celery import shared_task
from django.core.mail import send_mail
from main.mailing import message_list_news, contact_list
from gameApp.settings.base import EMAIL_HOST_USER

@shared_task
def newsletter_subscription_error(email):
    send_mail(
        'Ошибка подписки на рассылку',
        'Вы уже подписаны на рассылку.',
        EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )

@shared_task
def newsletter_subscription(email):
    send_mail(
        'Подписка на рассылку',
        'Спасибо за подписку, каждую неделю вы будете получать письмо о свежих новостях!',
        EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )

@shared_task
def send_newsletter():
        send_mail(
            'Новостная рассылка',
            'Новости: ',
            EMAIL_HOST_USER,
            contact_list,
            html_message= message_list_news,
            fail_silently=False
    )