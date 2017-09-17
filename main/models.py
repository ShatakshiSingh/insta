from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='posts', default='media/default.jpg')
    likes = models.IntegerField(default=0)


    def save_post(self):
        self.save()

    def __str__(self):
        return self.title

