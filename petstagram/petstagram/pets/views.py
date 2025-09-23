from django.shortcuts import render, redirect
from petstagram.pets.forms import PetForm
from petstagram.pets.models import Pet

# Create your views here.
def add_pet(request):
    form = PetForm(request.POST or None, )
    if form.is_valid():
        form.save()
        return redirect('home')
    
    context={
        'form':form,
    }   
    return render(request, template_name='pets/pet-add-page.html', context=context)
    
    
def pet_details(request, username, pet_slug):
    pet=Pet.objects.get(slug=pet_slug,)
    all_photos=pet.photo_set.all()
    context={
        'pet':pet,
        'all_photos':all_photos,
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)

def edit_pet(request, username, pet_slug):
    from django.http import HttpResponse
    return HttpResponse("Edit pet page")

def delete_pet(request, username, pet_slug):
    pet=Pet.objects.get(slug=pet_slug,)
    if request.method=='POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    