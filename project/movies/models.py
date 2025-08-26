from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"


class Movie(models.Model):
    name = models.CharField(max_length=200, verbose_name="nomi")
    description = models.TextField(null=True, blank=True, verbose_name="Matni")
    photo = models.ImageField(upload_to='movies/photos/', verbose_name="rasmi")
    video = models.FileField(upload_to='movies/videos/', blank=True, null=True, verbose_name="videosi")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="movies", verbose_name="janr")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"
        ordering = ["-name"]
