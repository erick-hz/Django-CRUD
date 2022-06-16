from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books, name='books'),
    path('books/create', views.create, name='create'),
    path('books/edit', views.edit, name='edit'),
]