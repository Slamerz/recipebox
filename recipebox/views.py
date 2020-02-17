from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from recipebox.models import Author, Recipe
from recipebox.forms import AddAuthorForm, AddRecipeForm, LoginForm


def index(request):
    html = 'index.html'

    recipes = Recipe.objects.all()

    if request.user.is_authenticated:
        button_href = '/logout/'
        button_message = 'LOGOUT'
    else:
        button_href = '/login/'
        button_message = 'LOGIN'

    return render(
        request,
        html,
        {
            'recipes': recipes,
            'button_href': button_href,
            'button_message': button_message})


def recipe_view(request, id):
    html = 'recipe.html'

    recipe = Recipe.objects.get(pk=id)
    signed_in = request.user.is_authenticated

    return render(request, html, {'recipe': recipe, 'signed_in': signed_in})


def author_view(request, id):
    html = 'author.html'

    author = Author.objects.get(pk=id)
    recipes = Recipe.objects.filter(author=author)

    return render(request, html, {'author': author, 'recipes': recipes})


@login_required
def add_author_view(request):

    if not request.user.is_staff:
        # raise Exception('Must be an admin to add an author')
        messages.add_message(request, messages.INFO,
                             'Only Admin Users have permission to add authors.')
        return HttpResponseRedirect(reverse('homepage'))

    html = 'add_author.html'

    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            Author.objects.create(
                user=u,
                name=data['name'],
                bio=data.get('bio')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()

    return render(request, html, {'form': form})


@login_required
def add_recipe_view(request):
    html = 'add_recipe.html'

    if request.method == 'POST':
        form = AddRecipeForm(request.user, request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddRecipeForm(request.user)
    return render(request, html, {'form': form})


def login_view(request):
    html = 'login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )

        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required()
def favorite_view(request, id):
    author = Author.objects.get(user=request.user)
    recipe = Recipe.objects.get(pk=id)
    author.favorites.add(recipe)
    return HttpResponseRedirect(reverse('homepage'))


@login_required()
def unfavoritre_view(request, id):
    author = Author.objects.get(user=request.user)
    recipe = Recipe.objects.get(pk=id)
    author.favorites.remove(recipe)
    return HttpResponseRedirect(reverse('homepage'))

