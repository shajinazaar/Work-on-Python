from django.db.models.signals import post_save #This signals is fired when the object(user) is created
from django.contrib.auth.models import User #Here User model is our sender when the user is created.
from django.dispatch import receiver #The reciever is a function  which will recieve & perfrom something.
from .models import Profile


@receiver(post_save,sender=User)
def create_Profile(sender,instance,created,**kwagrs):
# **kwargs Its accepts an addtional keyword arguments at the end of the function
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_Profile(sender,instance,**kwagrs):
    instance.profile.save()
