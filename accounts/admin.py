from django.contrib import admin
from .models import *

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = [
		'email',
		'username',
		'name',
		'is_staff',
	]
	list_display_links = [
		'username',
	]
	fieldsets = UserAdmin.fieldsets + (
		(
			None, 
			{
			'fields':('name',)
			}
		),
	) 
	add_fieldsets = UserAdmin.add_fieldsets + (
		(
			None, 
			{
			'fields':('name',)
			}
		),
	)

#admin.site.register(CustomUser, CustomUserAdmin)