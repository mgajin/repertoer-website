from django.contrib import admin

from .models import Cinema


# Filtering
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 20

admin.site.register(Cinema, CinemaAdmin)
