from django.urls import path

from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='pet_add'),
    path('<str:username>/pet/<slug:pet_slug>/', views.pet_details, name='pet_details'),
    path('<str:username>/pet/<slug:pet_slug>/edit/', views.edit_pet, name='pet_edit'),
    path('<str:username>/pet/<slug:pet_slug>/delete/', views.delete_pet, name='pet_delete'),
]