from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_photo = models.URLField()
    date_of_birth = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=False, blank=False, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 🔥 эзэмшигч

    def save(self, *args, **kwargs):
        creating = self.pk is None  # Шинээр үүсгэж байна уу гэдгийг шалгах
        super().save(*args, **kwargs)  # Save first to get self.id

        expected_slug = slugify(f"{self.name}-{self.id}")
        if self.slug != expected_slug:
            self.slug = expected_slug
            super().save(update_fields=["slug"])  # Зөвхөн slug-г хадгалах

       
    def __str__(self):
        return self.name