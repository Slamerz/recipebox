"""
Author
    Name
    Bio (TextField)

Recipe
    Title
    Author (ForeignKey)
    Description
    Time Required
    Instructions (TextField)
"""

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField()
    favorites = models.ManyToManyField(
        'Recipe', related_name='favorites', symmetrical=False, blank=True
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.author.name}'
