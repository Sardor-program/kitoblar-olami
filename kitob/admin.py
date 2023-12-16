from django.contrib import admin
from kitob.models import Author, Category, Book, BookAuthor, SelectedBooks, Reviews

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(SelectedBooks)
admin.site.register(Reviews)

