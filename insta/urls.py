from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path(r'^home',views.home,name='home'),
    re_path(r'^signup',views.signup,name='signup'),
    re_path(r'^$',views.signin,name='signin'),
    re_path(r'^logout',views.logout,name='logout'),
    re_path(r'^upload',views.upload,name='upload'),
    re_path(r'^like-post',views.like_post,name='like-post'),
    re_path(r'^profile/(\d+)/$',views.profile,name='profile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    