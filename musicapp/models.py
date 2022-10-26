from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()


class Song(models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateTimeField()
    likes = models.PositiveIntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyrics(models.Model):
    content = models.TextField(blank=True, null=True)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
