__author__ = 'shawn'

from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'pools', views.PoolViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/',views.test),
    url(r'^reserve/(?P<id>[0-9])/',views.NewReservation,name="make_reserve"),
	url(r'^api/', include(router.urls),name="api"),
    url(r'^manage/books/$', views.book_list, name='book_list'),
    url(r'^manage/books/new/', views.book_create, name='book_new'),
    url(r'^manage/books/edit/(?P<pk>\d+)$', views.book_update, name='book_edit'),
    url(r'^manage/books/delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),
]
