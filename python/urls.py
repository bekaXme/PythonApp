from django.urls import path
from . import views

urlpatterns = [
    path('', views.python_list, name='python_list'),
    path('create/', views.python_create, name='python_create'),
    path('update/<int:pk>/', views.python_update, name='python_update'),
    path('delete/<int:pk>/', views.python_delete, name='python_delete'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('register/', views.register, name='register'),
]