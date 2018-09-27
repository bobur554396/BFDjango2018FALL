from django.forms import ModelForm
from main.models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')
