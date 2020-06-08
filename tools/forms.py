from django import forms
from webnotes.models import Tool


class ToolForm(forms.ModelForm):
    name = forms.CharField(label='Вид инструмента', help_text='Например, спицы, крючек,..')
    size = forms.FloatField(label='Размер, мм')
    producer = forms.CharField(label='Фирма производитель')
    type = forms.CharField(label='Тип инструмента', help_text='Круговые, прямые, чулочные,..')
    material = forms.CharField(label='Материал инструмента', help_text='Металлические, деревянные,..')

    class Meta:
        model = Tool
        fields = ('name', 'size', 'producer', 'type', 'material', 'user')


class ToolForm2(forms.ModelForm):
    name = forms.CharField(label='Вид инструмента', help_text='Например, спицы, крючек,..')
    size = forms.FloatField(label='Размер, мм')
    producer = forms.CharField(label='Фирма производитель')
    type = forms.CharField(label='Тип инструмента', help_text='Круговые, прямые, чулочные,..')
    material = forms.CharField(label='Материал инструмента', help_text='Металлические, деревянные,..')

    class Meta:
        model = Tool
        fields = ('name', 'size', 'producer', 'type', 'material')
