from django.contrib import admin

from app_books.models import AuthorModel, BookModel

admin.site.register(AuthorModel)
admin.site.register(BookModel)
