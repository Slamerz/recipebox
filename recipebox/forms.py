from django import forms
from recipebox.models import Recipe, Author


class AddAuthorForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['author', 'title', 'description',
                  'time_required', 'instructions']

    def __init__(self, user, *args, **kwargs):
        super(AddRecipeForm, self).__init__(*args, **kwargs)
        if not user.is_staff:
            self.fields['author'].queryset = Author.objects.filter(user=user)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
