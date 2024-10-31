from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_books.models import AuthorModel
from app_books.serializers import AuthorModelSerializer


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        authors = AuthorModel.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AuthorModelSerializer(data=request.data, instance='author')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'success': True, 'message': 'Post Successfully', "data": serializer.data}
        return Response(response, status=201)
    else:
        return HttpResponse("Invalid request method", status=405)

@api_view(['PUT', 'DELETE', 'PATCH'])