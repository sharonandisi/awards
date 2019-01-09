from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewImageForm, ReviewForm, UpdateProfile
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Image, Review
from django.urls import reverse
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ImageSerializer


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()

    return render(request, 'index.html', { "images":images})

def search_results(request):
    if 'image' in request.GET and request.get["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"
        
        return render(request, 'all-photos/search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message":message})

def image(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user)
    image = Image.objects.get(id = id)
    reviews = Review.objects.filter(image = image)
    design = reviews.aggregate(Avg('design'))['design__avg']
    usability = reviews.aggregate(Avg('usability'))['usability__avg']
    content = reviews.aggregate(Avg('content'))['content__avg']
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit = False)
            review.average = review.design + review.usability + review.content
            review.image = image
            review.user = user
            review.save()
        return redirect('image', id)
    else:
        form = ReviewForm()
    return render(request, 'all-photos/proj.html', {"image": image, "reviews": reviews, "form": form, "design": design, "usability": usability, "content": content})

@login_required(login_url='/accounts/login/')
def upload_image(request):
    if request.method == 'POST':
        form = NewImageForm(request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
        return redirect('index')
    else:
        form = NewImageForm()

    return render(request, 'upload.html', {'form': form})




@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user =  request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form":form})

def profile(request, user_id):
    images = Image.objects.filter(user_id= user_id)
    profile = Profile.objects.get(id = id)
    return render(request, 'all-photos/profile.html', {"images":images, "profile":profile})

@login_required(login_url='/accounts/login/')
def profile_edit(request, user_id):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile', user_id)
        else:
            messages.error(request, ('Error'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request,'all-photos/edit_profile.html',{"profile_form":profile_form})

class ListProfiles(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ListImages(APIView):
    def get(self, request, format=None):
        all_images = Image.objects.all()
        serializers =  ImageSerializer(all_projects, many=True)
        return Response(serializers.data)

    