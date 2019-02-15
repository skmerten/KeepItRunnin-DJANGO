from django.db import models
from app.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.IntegerField(null = False)

    def __str__(self):
        return self.user
