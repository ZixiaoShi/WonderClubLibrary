from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
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

    def __unicode__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=255, verbose_name='Title')
    alt_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Alternative Title')
    sub_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Sub Title')
    isbn = models.CharField(default='0', max_length=255, verbose_name='ISBN13')
    author = models.CharField(default='author', max_length=255, verbose_name='Author')
    translator = models.CharField(max_length=255, blank=True, null=True, verbose_name='Translator')
    publisher = models.CharField(max_length=255, blank=True, null=True, verbose_name='Publisher')
    pubdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Published Date')
    pages = models.IntegerField(default=0, blank=True, null=True, verbose_name='Pages')
    donor = models.ForeignKey(User, null=True, blank=True, related_name='Donor')
    recommender = models.ManyToManyField(User,null=True,blank=True, related_name='Recommender')
    local_avail = models.BooleanField(default=True, verbose_name='Local Availability')
    notes = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Notes')
    tags = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Tags')
    pool = models.ForeignKey(Pool,verbose_name='Pool',null=True)
    pool_date = models.DateField(auto_now=False, null=True, verbose_name='Pool Date')
    renter = models.ForeignKey(User, null=True, blank=True, related_name='Renter')
    duedate = models.DateField(blank=True, null=True, verbose_name='Due Date')
    book_number = models.CharField(default="0",max_length=255, verbose_name='Book Number')

    def __unicode__(self):
        return self.title


class Reservation(models.Model):
    book = models.ForeignKey(Book, null=True, verbose_name="Book")
    borrower = models.ForeignKey(User, null=True, verbose_name="Borrower")
    request_date = models.DateField(auto_now=True, null=True, verbose_name="Request Date")
    pickup_date = models.DateField(auto_now=False, null=True, verbose_name="Pickup Date")
    picked_up = models.BooleanField(default=False, verbose_name="Picked Up Status")
    due_date = models.DateField(auto_now=False, null=True, verbose_name="Due Date")
    returned = models.BooleanField(default=False, verbose_name="Returned Status")
    return_date = models.DateField(auto_now=False, null=True, verbose_name="Return Date")
