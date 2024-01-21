from django.contrib import admin
from rest_api.models import Book


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
