from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", 
                  {
                      "books": books
                  })


def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, pk=id)

    return render(request, "book_outlet/book_detail.html",
                  {
                      "title": book.title,
                      "author": book.author,
                      "is_bestselling": book.is_bestselling,
                      "rating": book.rating
                  })