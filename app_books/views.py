from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_books.models import AuthorModel, BookModel
from app_books.serializers import AuthorModelSerializer, BookModelSerializer

authors = AuthorModel.objects.all()
products = BookModel.objects.all()


@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
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
def author_detail(request, pk):
    try:
        author = AuthorModel.objects.get(pk=pk)
    except AuthorModel.DoesNotExist:
        return HttpResponse("Author not found", status=404)
    if request.method == 'GET':
        serializer = AuthorModelSerializer(author, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AuthorModelSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'success': True, 'message': 'Put Successfully', "data": serializer.data}
        return Response(response, status=200)
    elif request.method == 'DELETE':
        author.delete()
        return Response({'success': True, 'message': 'Delete Successfully'}, status=204)
    elif request.method == 'PATCH':
        serializer = AuthorModelSerializer(author, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'success': True, 'message': 'Patch Successfully', "data": serializer.data}
        return Response(response, status=200)
    else:
        return HttpResponse("Invalid request method", status=405)


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = BookModel.objects.all()
        serializer = BookModelSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookModelSerializer(data=request.data, instance='book')
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'success': True, 'message': 'Post Successfully', "data": serializer.data}
        return Response(response, status=201)
    else:
        return HttpResponse("Invalid request method", status=405)


@api_view(['PUT'])
def book_update(request, pk):
    product = get_object_or_404(BookModel, pk=pk)
    if request.method == 'PUT':
        serializer = BookModelSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'success': True, 'message': 'Put Successfully', "data": serializer.data}
        return Response(response, status=200)


@api_view(['DELETE'])
def book_delete(request, pk):
    product = get_object_or_404(BookModel, pk=pk)
    if request.method == 'DELETE':
        product.delete()
        return Response({'success': True, 'message': 'Delete Successfully'}, status=204)


@api_view(['PATCH'])
def book_updates(request, pk):
    product = get_object_or_404(BookModel, pk=pk)
    if request.method == 'PATCH':
        serializer = BookModelSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {'success': True, 'message': 'Patch Successfully', "data": serializer.data}
        return Response(response, status=200)
    else:
        return HttpResponse("Invalid request method", status=405)
