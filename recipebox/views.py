from django.shortcuts import render, HttpResponseRedirect, reverse

from recipebox.models import Author, Recipe
from recipebox.forms import AddAuthorForm, AddRecipeForm


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


def add_author_view(request):
    html = 'add_author.html'

    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()

    return render(request, html, {'form': form})


def add_recipe_view(request):
    html = 'add_recipe.html'

    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                author=data['author'],
                title=data['title'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeForm()
    return render(request, html, {'form': form})
