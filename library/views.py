from django.http import HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, filters
from .serializer import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import TabHolder, Tab, FieldWithButtons, StrictButton

# Library Home View.
@login_required
def index(request):
    all_books_list = Book.objects.order_by('id')[:5]
    context = {
        'all_books_list': all_books_list,
    }
    return render_to_response('library/index.html', context)


def test(request):
    context = {}
    return render_to_response('library/gCalendarTest.html',context)


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#Django Forms for editing books, staff only
class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "id-BookForm"
        self.helper.form_method = 'post'
        self.form_action = 'submit'
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    'Basic Information',
                    FieldWithButtons('isbn',StrictButton('Read Information from Douban',id='readISBN')),
                    'title',
                    'alt_title',
                    'sub_title',
                    'author',
                    'translator',
                    'publisher',
                    'pubdate',
                    'pages'
                ),
                Tab(
                    'Book Pool Information',
                    'donor',
                    'recommender',
                    'local_avail',
                    'notes',
                    'tags',
                    'pool',
                    'pool_date',
                    'book_number',
                    'renter',
                    'duedate'
                )
            )
        )
        self.helper.add_input(Submit('submit','Submit'))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.fields['pool'].required = True

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
    dic = {'form':form,
           'Access-Control-Allow-Origin':'*',
           'Access-Control-Allow-Methods':"GET",
           'Access-Control-Allow-Headers':'*'
        }
    return render(request, template_name, dic)

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
@login_required
class PoolViewSet(viewsets.ModelViewSet):
    queryset = Pool.objects.all()
    serializer_class = PoolSerializer


@login_required
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('title', 'isbn', 'author', 'id','book_number')
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter)
    search_fields = ('title', 'author', 'book_number')

#Reservation Views
@login_required
def NewReservation(request, id):
    try:
        book = Book.objects.get(id=id)
    except:
        return HttpResponse("No Book Found")
    if book.local_avail == False:
        return HttpResponse("Book Unavailable")

    return HttpResponse("success")
