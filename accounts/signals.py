from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(instance,created,sender,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def update_profile(instance,sender,**kwargs):
    instance.profile.save()
