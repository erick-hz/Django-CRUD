from django.shortcuts import render
from.models import Book
from .forms import BookForm

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books/index.html' , {'books': books})

def create(request):
    form = BookForm(request.POST or None)
    return render(request, 'books/create.html' , {'form': form})

def edit(request):
    return render(request, 'books/edit.html')

