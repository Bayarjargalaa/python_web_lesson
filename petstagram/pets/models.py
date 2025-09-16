from django.db import models
from django.template.defaultfilters import slugify

class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_photo = models.URLField()
    date_of_birth = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save first to get self.id
        # Slug: name + id, separated by "-"
        expected_slug = slugify(f"{self.name}-{self.id}")
        if self.slug != expected_slug:
            self.slug = expected_slug
            return super().save(*args, **kwargs)
        return

    def __str__(self):
        return self.name