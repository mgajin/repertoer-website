from django.db import models
from cinemas.models import Cinema

class Movie(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=200)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    released = models.IntegerField()
    runtime = models.IntegerField()
    ticket_price = models.IntegerField()
    poster = models.ImageField(upload_to='posters/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title