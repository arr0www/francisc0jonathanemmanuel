from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:status>/', views.home, name = 'home'),
    path('done/<int:pk>/', views.done, name='done'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('add/', views.add, name = 'add'),
    path('update/<int:pk>/', views.update, name='update'),
]