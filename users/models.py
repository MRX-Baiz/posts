from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.png',
        upload_to='profile',  # Sera servi depuis /media/profile/
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])]
    )

    def __str__(self):
        return f"Profile(user={self.user.username}, image={self.image.name})"
