from django.contrib import admin
from .models import Image, Profile, LikePost

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(LikePost)