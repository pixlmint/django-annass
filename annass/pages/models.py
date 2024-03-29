from django.db import models

# Create your models here.
from django.db.models import EmailField, URLField, ImageField
from martor.models import MartorField


class UeberMich(models.Model):
    profile_image = ImageField(upload_to="profile_iamges", verbose_name="Profilbild", null=True, blank=True)
    text = MartorField()

    def __str__(self):
        return 'Über mich'


class Kontakt(models.Model):
    email_address = EmailField(verbose_name='Email Adresse', blank=True)
    facebook = URLField(blank=True)
    instagram = URLField(blank=True)
    pinterest = URLField(blank=True)

    def __str__(self):
        return 'Kontakt'