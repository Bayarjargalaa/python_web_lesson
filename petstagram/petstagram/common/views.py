from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy
from petstagram.common.forms import CommentForm, SearchForm
from petstagram.common.models import Like

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Create your views here.

def home(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form=SearchForm(request.GET)
    all_pets = Pet.objects.all()
    print(all_pets[1].__dict__)
    
    
    if search_form.is_valid():
        all_photos=all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])
    
    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
        'search_form': search_form,
        'all_pets': all_pets,
        
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
    copy(request.META['HTTP_HOST']+resolve_url('photo_details', photo_id))
    # url = request.build_absolute_uri(resolve_url('photo_details', photo_id))
    # copy(url)  # анхаар: энэ серверийн клипбоард дээр хуулна
    return redirect(request.META['HTTP_REFERER']+f'#{photo_id}')

def add_comment(request, photo_id):
    if request.method == 'POST':
        photo=Photo.objects.get(id=photo_id)
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.to_photo=photo
            comment.save()
    return redirect(request.META['HTTP_REFERER']+f'#{photo_id}')
        