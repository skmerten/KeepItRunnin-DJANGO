from django.db import models
from app.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=False)
    post = models.TextField()

    def __str__(self):
        return self.user + " " + self.date
