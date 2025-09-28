from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    ]

    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            RegexValidator(r'^[A-Za-z]+$', 'Only letters are allowed.')
        ]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            RegexValidator(r'^[A-Za-z]+$', 'Only letters are allowed.')
        ]
    )
    profile_picture = models.URLField(blank=True)
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, default='Do not show')

    def __str__(self):
        return self.username