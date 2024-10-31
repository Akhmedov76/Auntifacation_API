# AuthorModelSerializer
from rest_framework import serializers

from app_books.models import AuthorModel, BookModel


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
