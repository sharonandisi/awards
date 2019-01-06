from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()


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

@login_required(login_url=)