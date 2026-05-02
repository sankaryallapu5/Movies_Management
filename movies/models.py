from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class movie_Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imdb_id = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    poster = models.URLField(blank=True)
    year = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
