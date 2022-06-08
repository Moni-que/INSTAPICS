from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    id_user = models.IntegerField(default='')
    profile_photo = models.ImageField(upload_to = 'profile_images', blank=True)
    bio = models.TextField(blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.bio

class Image(models.Model):
    image = models.ImageField(upload_to = 'post_images')
    image_name = models.CharField(max_length = 30)
    image_caption = models.TextField(max_length = 100, blank=True)
    Likes = models.IntegerField(default= 0,blank=True)

    def __str__(self):
        return self.image_caption