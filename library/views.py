from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, viewsets, renderers, filters
from .serializer import *

# Create your views here.
def index(request):
    all_books_list = Book.objects.order_by('id')[:5]
    context = {
        'all_books_list': all_books_list,
    }
    return render_to_response('library/index.html', context)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('title', 'isbn', 'author',)
    filter_backends = (filters.DjangoFilterBackend,)

