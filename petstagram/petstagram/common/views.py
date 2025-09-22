from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from petstagram.photos.models import Photo
from petstagram.photos.models import Like

# Create your views here.

def home(request):
    all_photos = Photo.objects.all()
    context = {
        'all_photos': all_photos,
    }
    return render(request, template_name='common/home-page.html', context=context)

def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object=Like.objects.filter(to_photo_id=photo_id, user=request.user).first()
    if liked_object:
        liked_object.delete()
    else:
        like=Like(to_photo=photo,)
        like.save()
    return redirect(request.META['HTTP_REFERER']+f'#{photo_id}')

def copy_link_to_clipboard(request, photo_id):
    # copy(request.META['HTTP_HOST']+resolve_url('photo_details', *args: photo_id))
    url = request.build_absolute_uri(resolve_url('photo_details', photo_id))
    copy(url)  # анхаар: энэ серверийн клипбоард дээр хуулна
    return redirect(request.META['HTTP_REFERER']+f'#{photo_id}')
        