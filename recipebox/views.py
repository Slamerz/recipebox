from django.shortcuts import render

from recipebox.models import Author, Recipe


def index(request):
    html = 'index.html'

    recipes = Recipe.objects.all()

    return render(request, html, {'recipes': recipes})


def recipe_view(request, id):
    html = 'recipe.html'

    recipe = Recipe.objects.get(pk=id)

    return render(request, html, {'recipe': recipe})


def author_view(request, id):
    html = 'author.html'

    author = Author.objects.get(pk=id)
    recipes = Recipe.objects.filter(author=author)

    return render(request, html, {'author': author, 'recipes': recipes})
