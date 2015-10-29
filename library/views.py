from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, filters
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

#Django Forms for editing books, staff only
class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = []

@staff_member_required
def book_list(request, template_name='library/book_list.html'):
    books = Book.objects.all()
    data = {}
    data['object_list'] = books
    return render(request, template_name, data)


@staff_member_required
def book_create(request, template_name='library/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

@staff_member_required
def book_update(request, pk, template_name='library/book_form.html'):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

@staff_member_required
def book_delete(request, pk, template_name='library/book_confirm_delete.html'):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object':book})


#Django Rest API View Sets
class PoolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('title', 'isbn', 'author',)
    filter_backends = (filters.DjangoFilterBackend,)

