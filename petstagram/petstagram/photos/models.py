from django.conf import settings
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
    
class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user} on photo {self.photo_id}"