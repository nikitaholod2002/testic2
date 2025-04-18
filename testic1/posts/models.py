from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    full_text = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="Другое")
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-data_create']

    def __str__(self):
        return  self.name


class Comment(models.Model):
    text = models.CharField(max_length=100)
    data_create = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['data_create']

    def __str__(self):
        return f'{self.post.name} and {self.author}'