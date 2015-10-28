__author__ = 'shawn'

from rest_framework import serializers
from .models import *

class PoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pool

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book