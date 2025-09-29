from django.urls import path

from petstagram.pets import views

urlpatterns = [
    # path('add/', views.add_pet, name='pet_add'),
    path('add/', views.PetAddView.as_view(), name='pet_add'),
    # path('<str:username>/pet/<slug:pet_slug>/', views.pet_details, name='pet_details'),
    path('<str:username>/pet/<slug:pet_slug>/', views.PetDetailsView.as_view(), name='pet_details'),
    # path('<str:username>/pet/<slug:pet_slug>/edit/', views.edit_pet, name='edit_pet'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', views.PetEditView.as_view(), name='edit_pet'),
    # path('<str:username>/pet/<slug:pet_slug>/delete/', views.delete_pet, name='delete_pet'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', views.PetDeleteView.as_view(), name='delete_pet'),
]