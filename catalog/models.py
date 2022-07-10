import uuid
from datetime import date

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Language(models.Model):

    language = models.CharField(max_length=10)

    class Meta:
        ordering = ["language"]

    def __str__(self):
        return self.language


class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, null=True)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    date_of_death = models.DateField("Died", blank=True, null=True)

    class Meta:
        ordering = ["last_name"]
        permissions = (
            ("can_crud", "Can C.R.U.D for Authors"),
        )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Book(models.Model):
    tittle = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null= True)
    summary = models.CharField(max_length=200)
    genre_list = models.ManyToManyField(Genre)

    class Meta:
        ordering = ["tittle"]
        permissions = (
            ("can_crud", "Can C.R.U.D for Books"),
        )

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre_list.all()[:3]])

    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    borrowed = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='m',
    help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]
        permissions = (
            ("can_make_returned", "Set book as returned"),
            ("can_see_all_onloan", "Can see all book instances status on loan"),
            ("can_renew", "Can renew borrowed books")
        )

    def __str__(self):

        return f"{self.book.tittle} ID: {self.id}"
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False