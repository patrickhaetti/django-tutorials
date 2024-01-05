from django.contrib import admin

from .models import Book, Author, Address

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",) # not possible when prepopulated_fields
    prepopulated_fields = {"slug": ("title",)}  # editable=False not possible in Book model then
    list_filter = ("title","author","rating")
    list_display = ("title","author")

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)