from django.urls import path

from app_books import views

app_name = "books"

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('create/<int:pk>/', views.author_detail, name='author_detail'),
    path('update/<int:pk>/', views.author_detail, name='author_update'),
    path('delete/<int:pk>/', views.author_detail, name='author_delete'),
    path('books/', views.book_list, name='book_list'),
    path('books/update/<int:pk>/', views.book_update, name='book_update'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('books/patch/<int:pk>/', views.book_updates, name='book_create'),
]
