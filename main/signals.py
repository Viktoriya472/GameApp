from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from main.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = User.objects.get(id=instance.id)
    profile = Profile()
    if created:
        profile.user = user
        profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
