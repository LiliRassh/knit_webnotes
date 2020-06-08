from django import forms
from webnotes.models import Yarn


class YarnForm(forms.ModelForm):
    name = forms.CharField(label='Название пряжи')
    color_lot = forms.CharField(label='Цвет пряжи или COLOR - LOT', help_text='Например: 141 - 368700')
    weight = forms.IntegerField(label='Вес, гр')
    length = forms.IntegerField(label='Длина, м')
    label = forms.FileField(label='Фото этикетки')
    source = forms.URLField(label='Сайт магазина', help_text='Ссылка на сайт магазина или на обзор пряжи')

    class Meta:
        model = Yarn
        fields = ('name', 'color_lot', 'weight', 'length', 'label', 'source', 'user')


class YarnForm2(forms.ModelForm):
    name = forms.CharField(label='Название пряжи, фирмы')
    color_lot = forms.CharField(label='Цвет пряжи или COLOR - LOT', help_text='Например: 141 - 368700')
    weight = forms.IntegerField(label='Вес')
    length = forms.IntegerField(label='Длина')
    label = forms.FileField(label='Фото этикетки')
    source = forms.URLField(label='Ссылка на ресурс', help_text='Ссылка на сайт магазина или на обзор пряжи')

    class Meta:
        model = Yarn
        fields = ('name', 'color_lot', 'weight', 'length', 'label', 'source')
