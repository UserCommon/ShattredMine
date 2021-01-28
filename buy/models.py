from django.db import models
from accounts.models import Profile
from django.urls import reverse


class PlayerClaim(models.Model):
    name = models.CharField(blank=False, max_length=60)
    vk = models.CharField(blank=False, max_length=70, null=True)
    description = models.TextField(blank=False, max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('current_form_url', kwargs={'id': self.id})

    def __str__(self):
        return self.profile

# Create your models here.
