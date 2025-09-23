from django.db import models

from petstagram.photos.models import Photo

# Create your models here.

class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='likes')    
    def __str__(self):
        return f"Like by {self.user} on photo {self.photo_id}"
    
    

class Comment(models.Model):
    text=models.TextField(max_length=300)
    date_time_of_publication=models.DateTimeField(auto_now_add=True)
    to_photo=models.ForeignKey(Photo, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date_time_of_publication']