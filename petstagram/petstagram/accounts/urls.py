from django.urls import path, include
from petstagram.accounts import views


urlpatterns = [
    path('register/', views.register, name='register_user'),
    path('login/', views.login, name='login_user'),
    path("logout/", views.logout_user, name="logout_user"),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile_details'),
        path('edit/', views.edit_profile, name='profile_edit'),
        path('delete/', views.delete_profile, name='profile_delete'),   
             
    ])),
]
