from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewImageForm, ReviewForm, UpdateProfil
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
from .serializer import ProfileSerializer, ProjectSerializer


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    if User.objects.filter(username = request.user.username).exists():
        user = User.objects.get(username=request.user)
        if not Image.objects.filter(user = request.user).exists():
             Image.objects.create(user = user)
    images = Image.objects.order_by('-pub-date')
    return render(request,"index.html",{"images":images})



def search_results(request):
    if 'image' in request.GET and request.get["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"
        
        return render(request, 'all-photos/search.html', {"message":message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html', {"message":message})



@login_required(login_url='/accounts/login/')
def new_image(request, user_id):
    current_user =  request.user
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.developer = current_user
            image.save()
        return redirect('present')

    else:
        form = ImageUpload()
    return render(request, 'new_project.html', {"form":form})

def profile(request, user_id):
    images = Image.objects.all()
    return render(request, 'all-photos/profile.html', {"images":images})

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
        profile_form = ProfileForm
        (instance=request.user.profile)
    return render(request,'all-photos/edit_profile.html',{"profile_form":profile_form})
