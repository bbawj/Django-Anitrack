from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class AnimeInfo(models.Model):
    title = models.CharField(max_length=100)
    latest_ep_num = models.FloatField()
    ld = models.BooleanField()
    sd = models.BooleanField()
    hd = models.BooleanField()
    fhd = models.BooleanField()
    following_ld = models.ManyToManyField(User, related_name = 'following_ld', blank=True)
    following_sd = models.ManyToManyField(User, related_name = 'following_sd', blank=True)
    following_hd = models.ManyToManyField(User, related_name = 'following_hd', blank=True)
    following_fhd = models.ManyToManyField(User, related_name = 'following_fhd', blank=True)


    class Meta:
        constraints = [models.UniqueConstraint(fields = ['title'], name='unique_anime')]

    def validate_unique(self, exclude=None):
        super().validate_unique(exclude='title')

    def save(self, *args, **kwargs):
        try:
            anime = AnimeInfo.objects.get(title=self.title)
            self.id = anime.id
            super().save(*args, **kwargs, update_fields=["latest_ep_num","ld","sd","hd","fhd"])

        except AnimeInfo.DoesNotExist:
            super().save(*args, **kwargs)
