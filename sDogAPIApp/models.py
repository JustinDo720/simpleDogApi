from django.db import models


# Create your models here.
class Dog(models.Model):
    dog_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dog_img', blank=True, null=True)
    owner_name = models.CharField(max_length=100)
    shared_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dog_name