"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipebox import views
from recipebox.models import Author, Recipe

admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('recipes/<int:id>', views.recipe_view, name='recipes'),
    path('authors/<int:id>', views.author_view, name='authors'),
    path('addauthor/', views.add_author_view, name='addauthor'),
    path('addrecipe/', views.add_recipe_view, name='addrecipe'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('favorite/<int:id>', views.favorite_view, name='favorite'),
    path('unfavorite/<int:id>', views.unfavoritre_view, name='unfavorite')
]
