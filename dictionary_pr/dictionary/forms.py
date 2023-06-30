from django.forms import ModelForm, TextInput, Textarea, FileInput

from dictionary.models import Word


class DictForm(ModelForm):
    class Meta:
        model = Word
        fields = ['name', 'text', 'photo']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Слово',
                'width': '500px'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Отпределение слова',
                'width': '500px'
            }),
            "photo": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Изображение',
                'width': '500px'
            }),
        }
