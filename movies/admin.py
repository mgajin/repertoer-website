from django.contrib import admin

from .models import Movie

# Filtering
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'rating')
    list_dispplay_links = ('id', 'title')
    list_filter = ('cinema',)
    # list_editable = ('is_published',)
    search_fields = ('title', 'genre')
    list_per_page = 20

admin.site.register(Movie, MovieAdmin)