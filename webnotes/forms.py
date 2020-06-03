from django import forms
from .models import Webnote


class WebnoteForm(forms.ModelForm):
    project_name = forms.CharField(label='Название проекта')
    start_date = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Дата окончания', widget=forms.SelectDateWidget)
    for_who = forms.CharField(label='Для кого')
    image = forms.FileField(label='Фото изделия')
    private_status = forms.ChoiceField(label='Доступ другим пользователям',
                                       choices=((1, "Приватный"), (2, "Публичный")), widget=forms.RadioSelect)
    note = forms.CharField(label='Описание проекта', widget=forms.Textarea)

    class Meta:
        model = Webnote
        fields = ('project_name', 'start_date', 'end_date', 'for_who', 'craft', 'image',
                  'private_status', 'note', 'status', 'tool', 'pattern', 'yarn')


class WebnoteForm2(forms.ModelForm):
    project_name = forms.CharField(label='Название проекта')
    start_date = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Дата окончания', widget=forms.SelectDateWidget)
    for_who = forms.CharField(label='Для кого')
    # craft = forms.CharField(label='Вид рукоделия')
    private_status = forms.ChoiceField(label='Доступ другим пользователям',
                                       choices=((1, "Приватный"), (2, "Публичный")), widget=forms.RadioSelect)
    note = forms.CharField(label='Описание проекта', widget=forms.Textarea)

    class Meta:
        model = Webnote
        fields = ('project_name', 'start_date', 'end_date', 'for_who', 'craft', 'private_status', 'note', 'status',
                  'tool', 'pattern', 'yarn')
