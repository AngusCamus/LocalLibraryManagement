from uuid import UUID
from django.test import TestCase
from catalog.models import Author, Book, BookInstance

class AuthorModelTest(TestCase):

    def test_date_of_death_field(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'Died')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name,str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(),'/catalog/author/1')

class BookModelTest(TestCase):

    def test_title_max_length(self):
        book=Book.objects.get(id=1)
        title_field_max_lenght = book._meta.get_field("tittle").max_lenght
        self.assertEquals(title_field_max_lenght,100)

    def test_summary_max_length(self):
        book=Book.objects.get(id=1)
        summary_max_lenght = book._meta.get_field("summary").max_lenght
        self.assertEquals(summary_max_lenght,100)

    def test_get_absolute_url(self):
        book=Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(),'/catalog/book/1')

