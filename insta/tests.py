from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, LikePost

# Create your tests here.

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='myname')
        self.profile = Profile.objects.create(user = self.user,bio = 'mybio')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('myname')
        self.assertTrue(len(profile) > 0)

class ImageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='myname')
        self.profile = Profile.objects.create(user = self.user, bio = 'mybio')

        self.image = Image.objects.create( profile = self.profile, image_caption ='mylifestyle', no_of_likes = 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_get_images(self):
        self.image.save()
        image = Image.get_images()
        self.assertTrue(len(image) == 1)

