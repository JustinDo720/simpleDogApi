from django.db import models


# Create your models here.
class Dog(models.Model):
    dog_name = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='dog_img/', blank=True, null=True)
    owner_name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.dog_name:
            return self.dog_name
        else:
            return '?'