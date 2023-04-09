from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of stat'
            }),
            'intro': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Intro'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of pub'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of stat'
            })
        }