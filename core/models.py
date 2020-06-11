from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.CharField(max_length=10000)
    genres = models.CharField(max_length=10000)
    release_date = models.CharField(max_length=10)
    runtime = models.CharField(max_length=4)
    original_language = models.CharField(max_length=10000)
    spoken_language = models.CharField(max_length=10000)
    production_companies = models.CharField(max_length=10000)
    production_countries = models.CharField(max_length=10000)
    popularity = models.CharField(max_length=10)
    tagline = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    homepage = models.CharField(max_length=100)
    def __str__(self):
        return self.title