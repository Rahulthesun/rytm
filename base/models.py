from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Playlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=200, null=True, blank=True)
    caption=models.TextField( null=True, blank=True)
    embed_code=models.CharField(max_length=300)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

