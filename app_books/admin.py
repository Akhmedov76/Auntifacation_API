from django.contrib import admin
from django.contrib.auth.models import Group

from app_books.models import AuthorModel, BookModel

admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.unregister(Group)
