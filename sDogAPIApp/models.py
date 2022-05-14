from django.db import models


# Create your models here.
class Dog(models.Model):
    dog_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dog_img/', blank=True, null=True)
    owner_name = models.CharField(max_length=100)

    def __str__(self):
        if self.dog_name:
            return self.dog_name
        else:
            return '?'