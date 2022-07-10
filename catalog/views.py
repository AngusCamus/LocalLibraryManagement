import datetime

from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import catalog.models
from .forms import RenewBookModelForm
from .models import Book, Author, BookInstance, Genre
from django.views.generic import detail, list

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a', Available)
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
    num_genres = Genre.objects.count()

    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        "num_genres" : num_genres,
        "num_visits": num_visits
    }

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request,'index.html', context)

@permission_required("catalog.can_renew")
def renew_book_librarian(request, pk):
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookModelForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['due_back']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('books-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookModelForm(initial={'due_back': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})

#List and Details Views
class BookListView(list.ListView):
    model = Book
    paginate_by = 10
    template_name = "catalog/book-list.html"

class AuthorListView(list.ListView):
    model = Author
    paginate_by = 10
    template_name = "catalog/author-list.html"

class BookDetailView(detail.DetailView):
    model = Book
    template_name = "catalog/templates/catalog/book-detail.html"

class AuthorDetailView(detail.DetailView):
    model = Author
    template_name = "catalog/author-detail.html"

#Views for LoanedBooks
class LoanedBooksListView(PermissionRequiredMixin, list.ListView):
    model = BookInstance
    template_name = "catalog/bookinstance_list_borrowed_employed.html"
    paginate_by = 7
    permission_required = "catalog.can_make_returned"

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

class LoanedBooksByUserListView(LoginRequiredMixin, list.ListView):

    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrowed=self.request.user).filter(status__exact='o').order_by('due_back')

#Views for C.R.U.D
class AuthorCreate(PermissionRequiredMixin,CreateView):
    model = Author
    fields = '__all__'
    permission_required="catalog.can_crud"

class AuthorUpdate(PermissionRequiredMixin,UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']
    permission_required = "catalog.can_crud"

class AuthorDelete(PermissionRequiredMixin,DeleteView):
    model = Author
    success_url = reverse_lazy('authors-list')
    permission_required = "catalog.can_crud"


class BookCreate(PermissionRequiredMixin,CreateView):
    model = Book
    fields = '__all__'
    permission_required="catalog.can_crud"

class BookUpdate(PermissionRequiredMixin,UpdateView):
    model = Book
    fields = "__all__"
    permission_required = "catalog.can_crud"

class BookDelete(PermissionRequiredMixin,DeleteView):
    model = Book
    success_url = reverse_lazy('books-list')
    permission_required = "catalog.can_crud"

class BookInstanceCreate(PermissionRequiredMixin,CreateView):pass
class BookInstanceUpdate(PermissionRequiredMixin,UpdateView):pass
class BookInstanceDelete(PermissionRequiredMixin,DeleteView):pass