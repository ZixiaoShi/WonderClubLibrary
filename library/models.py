from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
book:
	title
	alt_title
	sub_title
	isbn
	author
	translator
	publisher
	pubdate
	pages
	donor_user_foreign_key
	recommenders_foreign_key
	local_availability
	notes
	tags
	pool_year
	pool_foreign_key
	call_number: 0a98 (ID)
	pool_number: CAR0a98
	rented_user_foreign_key

pool:
	name:
	location:
	start_year:
"""

class Pool(models.Model):

    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=True)




class Book(models.Model):

    title = models.CharField(max_length=255)
    alt_title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    isbn = models.CharField(default='0', max_length=255)
    author = models.CharField(default='author', max_length=255)
    translator = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    pubdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    pages = models.IntegerField(default=0, blank=True, null=True)
    donor = models.ForeignKey(User, null=True, blank=True, related_name='donor')
    recommender = models.ManyToManyField(User, null=True, blank=True, related_name='recommender')
    local_avail = models.BooleanField(default=True)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    tags = models.CharField(max_length=1024, blank=True, null=True)
    pool = models.ForeignKey(Pool, null=True, blank=True)
    pool_date = models.DateField(auto_now=True, blank=True, null=True)
    renter = models.ForeignKey(User, null=True, blank=True, related_name='renter')
    duedate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


