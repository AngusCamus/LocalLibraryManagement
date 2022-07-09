from django.contrib import admin
from .models import Language, Book, BookInstance, Author, Genre

class BookInLine(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]
    inlines = [BookInLine]

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("tittle", "author", "display_genre")
    inlines = [BookInstanceInLine]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "due_back", "id", "language", "borrowed")
    list_filter = ("status", "due_back", "borrowed")
    fieldsets = (
        (None, {
            "fields": ("book", "imprint", "id", "language")
        }),
        ("Availability",{
            "fields": ("status", "due_back", "borrowed")
        })

    )
admin.site.register(Language)
admin.site.register(Genre)
