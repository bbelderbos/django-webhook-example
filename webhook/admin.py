from django.contrib import admin

from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'contact_number',
                    'what_date', 'other_specific_date', 'what_services')

