__author__ = 'shawn'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^manage/books/$', views.book_list, name='book_list'),
    url(r'^manage/books/new/', views.book_create, name='book_new'),
    url(r'^manage/books/edit/(?P<pk>\d+)$', views.book_update, name='book_edit'),
    url(r'^manage/books/delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),
]
