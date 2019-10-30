from django import forms
from recipebox.models import Recipe


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['author', 'title', 'description',
                  'time_required', 'instructions']
