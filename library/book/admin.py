from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "count", "authors_list", "year_of_publication"]
    search_fields = ["id", "name", "year_of_publication"]
    list_filter = ["id", "name", "authors"]

    @admin.display(description="Authors")
    def authors_list(self, obj):
        return ', '.join(str(author) for author in obj.authors.all())