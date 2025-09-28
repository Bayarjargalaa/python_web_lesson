from django.shortcuts import render, redirect

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo
# Create your views here.
def photo_add(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context={
        'form':form,
    }
    return render(request, template_name='photos/photo-add-page.html', context=context)

def photo_details(request, pk):
    photo=Photo.objects.get(pk=pk,)
    likes=photo.like_set.all()
    comments=photo.comment_set.all()
    context={
        'photo':photo,
        'likes':likes,
        'comments':comments,
    }
    return render(request, template_name='photos/photo-details-page.html', context=context)

def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)
    if form.is_valid():
        form.save()
        return redirect('photo_details', pk=pk)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, template_name='photos/photo-edit-page.html', context=context)

def photo_delete(request, pk):
    photo=Photo.objects.get(pk=pk,)
    photo.delete()
    return redirect('home')
