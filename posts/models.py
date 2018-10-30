from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length = 20)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True)
def __str__(self):
    return self.title
