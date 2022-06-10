import uuid
from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# User = get_user_model()

# Create your models here.
class Profile(models.Model):
    profile_photo = CloudinaryField('image', blank=True)
    bio = models.TextField(blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.bio

class Image(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(max_length=100, blank=True)
    no_of_likes = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.image_caption

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    def __str__(self):
        return self.username