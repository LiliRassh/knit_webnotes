from django import forms
from webnotes.models import Pattern


class PatternForm(forms.ModelForm):
    name = forms.CharField(label='Название узора', help_text='Должно быть уникальным')
    image = forms.FileField(label='Фото узора')
    scheme = forms.FileField(label='Фото схемы узора')
    description = forms.CharField(label='Описание узора', widget=forms.Textarea)
    source = forms.URLField(label='Ссылка на ресурс', help_text='Ссылка на сайт или мастер-класс')

    class Meta:
        model = Pattern
        fields = ('name', 'image', 'scheme', 'description', 'source')


class PatternForm2(forms.ModelForm):
    name = forms.CharField(label='Название узора', help_text='Должно быть уникальным')
    image = forms.FileField(label='Фото узора')
    scheme = forms.FileField(label='Фото схемы узора')
    description = forms.CharField(label='Описание узора', widget=forms.Textarea)
    source = forms.URLField(label='Ссылка', help_text='Ссылка на сайт, где есть информация об узоре')

    class Meta:
        model = Pattern
        fields = ('name', 'image', 'scheme', 'description', 'source')
