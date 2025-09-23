from django.urls import path

from petstagram.photos import views

urlpatterns = [
    path('add/', views.photo_add, name='photo_add'),
    path('<int:pk>/', views.photo_details, name='photo_details'),
    path('<int:pk>/edit/', views.photo_edit, name='photo_edit'),
    path('delete/<int:pk>/', views.photo_delete, name='photo_delete'),
]