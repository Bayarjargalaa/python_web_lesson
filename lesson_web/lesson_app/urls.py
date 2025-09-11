from django.urls import path
from lesson_app import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('department/<int:task_id>/', views.view_department, name='view_department'),
    path('department/<int:department_id>/', views.view_department_by_id, name='view_department_by_id'),
    path("department/<str:department_name>/", views.view_department_by_name, name="view_department_by_name"),
]
