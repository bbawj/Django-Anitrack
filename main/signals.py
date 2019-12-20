from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import AnimeInfo
from django.contrib.auth.models import User
from django.core.mail import send_mail



@receiver(pre_save, sender=AnimeInfo, dispatch_uid="my_unique_identifier")
def my_handler(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(id = instance.id)
    except AnimeInfo.DoesNotExist:
        return None


    if float(obj.latest_ep_num) < float(instance.latest_ep_num):
        if instance.ld == True:
            user_list = obj.following_ld.all()
            recipient_list = []
            for user in user_list:
                email = user.email
                recipient_list.append(email)
            send_mail(
                'An episode you were tracking is out!',
                f"Episode {instance.latest_ep_num} of {instance.title} is now available at 360p.",
                "brendan@anitrack.com",
                recipient_list,
                fail_silently=False
            )
        if instance.sd == True:
            user_list = obj.following_sd.all()
            recipient_list = []
            for user in user_list:
                email = user.email
                recipient_list.append(email)
            send_mail(
                'An episode you were tracking is out!',
                f"Episode {instance.latest_ep_num} of {instance.title} is now available at 480p.",
                "brendan@anitrack.com",
                recipient_list,
                fail_silently=False
            )
        if instance.hd == True:
            user_list = obj.following_hd.all()
            recipient_list = []
            for user in user_list:
                email = user.email
                recipient_list.append(email)
            send_mail(
                'An episode you were tracking is out!',
                f"Episode {instance.latest_ep_num} of {instance.title} is now available at 720p.",
                "brendan@anitrack.com",
                recipient_list,
                fail_silently=False
            )
        if instance.fhd == True:
            user_list = obj.following_fhd.all()
            recipient_list = []
            for user in user_list:
                email = user.email
                recipient_list.append(email)
            send_mail(
                'An episode you were tracking is out!',
                f"Episode {instance.latest_ep_num} of {instance.title} is now available at 1080p.",
                "brendan@anitrack.com",
                recipient_list,
                fail_silently=False
            )
    else:
        if not obj.ld == instance.ld:
            user_list = obj.following_ld.all()
            recipient_list = []
            for user in user_list:
                email = user.email
                recipient_list.append(email)
            send_mail(
                'An episode you were tracking is out!',
                f"Episode {instance.latest_ep_num} of {instance.title} is now available at 360p.",
                "brendan@anitrack.com",
                recipient_list,
                fail_silently=False
            )
        if not obj.sd == instance.sd:
            user_list = obj.following_sd.all()
            recipient_list = []
            for user in user_list:
                email = user.email
                recipient_list.append(email)
            send_mail(
                'An episode you were tracking is out!',
                f"Episode {instance.latest_ep_num} of {instance.title} is now available at 480p.",
                "brendan@anitrack.com",
                recipient_list,
                fail_silently=False
            )
        if not obj.hd == instance.hd:
            user_list = obj.following_hd.all()
            recipient_list = []
            for user in user_list:
                email = user.email
                recipient_list.append(email)
            send_mail(
                'An episode you were tracking is out!',
                f"Episode {instance.latest_ep_num} of {instance.title} is now available at 720p.",
                "brendan@anitrack.com",
                recipient_list,
                fail_silently=False
            )
        if not obj.fhd == instance.fhd:
            user_list = obj.following_fhd.all()
            recipient_list = []
            for user in user_list:
                email = user.email
                recipient_list.append(email)
            send_mail(
                'An episode you were tracking is out!',
                f"Episode {instance.latest_ep_num} of {instance.title} is now available at 1080p.",
                "brendan@anitrack.com",
                recipient_list,
                fail_silently=False
            )

        else:
            pass
