from email.mime import image
from django.shortcuts import render,redirect
from .models import Profile, Image
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
@login_required(login_url = "signin")
def home(request):
    user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)
    posts = Image.objects.all()
    return render(request, 'all_templates/home.html', {'posts': posts })

@login_required(login_url = "signin")
def upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image_upload')
        image_caption = request.POST['caption']

        new_post = Image.objects.create(image=image, image_caption= image_caption)
        new_post.save()
        return redirect('home')
    else:
        return redirect('home')
    # return render(request, 'all_templates/upload.html')

@login_required(login_url = "signin")
def like_post(request):
    pass

@login_required(login_url = "signin")
def profile(request,user_id):
    user_profile = Profile.objects.filter(id=user_id)
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.profile_photo
            bio = request.POST['bio']

            user_profile.profile_photo = image
            user_profile.bio = bio
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            bio = request.POST['bio']

            user_profile.profile_photo = image
            user_profile.bio = bio
            user_profile.save()

        return redirect('profile',user_id)


    return render(request, 'all_templates/profile.html', {'user_profile': user_profile})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #login user and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)


                #create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('profile')

        else:
            messages.info(request, 'Passwords must match')
            return redirect('signup')

    else:
        return render(request, 'all_templates/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')

    return render(request, 'all_templates/signin.html')

@login_required(login_url = "signin")
def logout(request):
    auth.logout(request)
    return redirect('signin')