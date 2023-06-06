from django.contrib import admin
from .models import *

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
	pass