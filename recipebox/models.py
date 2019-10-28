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


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

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
