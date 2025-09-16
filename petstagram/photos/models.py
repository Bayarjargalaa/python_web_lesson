from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator, ValidationError

def photo_file_size(value):
    limit = 5 * 1024 * 1024  # 5MB
    if value.size > limit:
        raise ValidationError('Photo file too large. Size should not exceed 5 MB.')

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='photos/',
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png']),
            photo_file_size,
        ]
    )
    description = models.TextField(
        max_length=300,
        validators=[MinLengthValidator(10)],
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    tagged_pets = models.ManyToManyField('pets.Pet', blank=True)
    date_of_publication = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photo {self.id}"