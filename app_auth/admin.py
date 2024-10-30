from django.contrib import admin

from app_auth.urls import LoanModel, UserModel


@admin.register(LoanModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'borrow_date', 'return_date')
    search_fields = ('user__username', 'book__title')
    list_filter = ('borrow_date', 'return_date')
    date_hierarchy = 'borrow_date'


@admin.register(UserModel)
class UserNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'date_joined')
