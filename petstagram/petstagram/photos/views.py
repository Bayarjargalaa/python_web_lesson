from django.shortcuts import render

from petstagram.photos.models import Photo
# Create your views here.
def photo_add(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return redirect('photo_details', photo.pk)
    else:
        form = PhotoForm()

    return render(request, 'photos/photo-add-page.html', {'form': form})

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

def photo_edit(request):
    return None

def delete_profile(request):
    return None
