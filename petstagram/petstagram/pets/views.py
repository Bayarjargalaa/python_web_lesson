from django.shortcuts import render, redirect
from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetForm
@login_required
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)  # commit=False гэж бичиж owner-г зааж өгнө
            pet.owner = request.user       # owner-г одоо логин хийсэн user-р зааж өгнө
            pet.save()

            # Redirect profile page руу
            return redirect('profile_details', pk=request.user.pk)

    else:
        form = PetForm()

    context = {'form': form}
    return render(request, 'pets/pet-add-page.html', context)
    
    
def pet_details(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug, owner__username=username)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)

def edit_pet(request, username, pet_slug):
    pet = get_object_or_404(
        Pet,
        slug=pet_slug,
        owner__username=username,
    )

    if request.method == 'GET':
        form = PetForm(instance=pet)
        context = {'form': form, 'pet': pet}
        return render(request, 'pets/pet-edit-page.html', context)

    form = PetForm(request.POST, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('pet_details', username=username, pet_slug=pet.slug)

    context = {'form': form, 'pet': pet}
    return render(request, 'pets/pet-edit-page.html', context)



@login_required
def delete_pet(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug, owner__username=username)

    if request.method == "POST":
        pet.delete()
        # Уг delete амжилттай болсны дараа хэрэглэгчийг өөр хуудас руу чиглүүлнэ
        return redirect('profile_details', pk=request.user.pk)

    # GET request ирвэл баталгаажуулах хуудсыг харуулна
    context = {'pet': pet}
    return render(request, 'pets/pet-delete-page.html', context)