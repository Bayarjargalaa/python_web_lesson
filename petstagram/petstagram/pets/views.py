from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetDeleteForm, PetForm
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

class PetAddView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('profile_details', kwargs={'pk': self.request.user.pk})

    
    
def pet_details(request, username, pet_slug):
    pet = get_object_or_404(Pet, slug=pet_slug, owner__username=username)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context)



class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'
    slug_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        # зөв username-ийн pets-ийг л буцаана
        return queryset.filter(owner__username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = self.get_object()
        all_photos = pet.photo_set.all()
        context['all_photos'] = all_photos
        return context

    
    

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



class PetEditView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    slug_field = 'slug'
    context_object_name = 'pet'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # зөв хэрэглэгчийн pets-ийг л хайна
        return queryset.filter(owner__username=self.kwargs['username'])
    
    def get_success_url(self):
        return reverse_lazy('pet_details', kwargs={
            'username': self.object.owner.username,  # шинэ slug авахын тулд owner username-г авах
            'pet_slug': self.object.slug,            # шинэ slug-г ашиглах
        })




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

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'
    
    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('profile_details', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        return Pet.objects.get(
            slug=self.kwargs['pet_slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        owner_pk = pet.owner.pk  # 👈 owner.pk-г авна
        pet.delete()
        return redirect(reverse('profile_details', kwargs={'pk': owner_pk}))