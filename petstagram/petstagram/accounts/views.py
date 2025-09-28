from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from petstagram.accounts.forms import RegisterForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from petstagram.accounts.models import UserProfile
from .forms import EditProfileForm, EditUserForm

# Create your views here.
def register(request):
    if request.method == "POST":
        print("POST keys:", request.POST.keys())
        form = RegisterForm(request.POST)
        print("form errors:", form.errors)
        if form.is_valid():
            form.save()
            return redirect("login_user")
    else:
        form = RegisterForm()

    return render(request, "accounts/register-page.html", {"form": form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("Authenticated user:", user)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login-page.html', {'error': 'Хэрэглэгчийн нэр эсвэл нууц үг буруу байна.'})
    return render(request, template_name='accounts/login-page.html')

      
User = get_user_model()
@login_required
def profile_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    pets = user.pet_set.all() if hasattr(user, "pet_set") else []
    photos = user.photo_set.all() if hasattr(user, "photo_set") else []
    context={
        "profile_user": user,
        "pets": pets,
        "photos": photos,
        "is_owner": request.user == user,
    }
    return render(request, 'accounts/profile-details-page.html',  context)


@login_required
def edit_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        user_form = EditUserForm(request.POST, instance=user)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_details', pk=user.pk)
    else:
        user_form = EditUserForm(instance=user)
        profile_form = EditProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/profile-edit-page.html', context)


def delete_profile(request):
    return None

def logout_user(request):
    auth_logout(request)  # хэрэглэгчийн session устгана
    return redirect('home')  # login хуудас руу буцаана (эсвэл өөр хуудас)