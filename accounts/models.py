from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    country = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    # Define choices for registration category
    LOCAL = 'Local'
    INTERNATIONAL = 'International'
    REGISTRATION_CATEGORY_CHOICES = [
        (LOCAL, 'Local'),
        (INTERNATIONAL, 'International'),
    ]

    registration_category = models.CharField(
        max_length=20,
        choices=REGISTRATION_CATEGORY_CHOICES,
        default=LOCAL,  # Set default to 'Local'
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    admin = models.BooleanField(default=False)
