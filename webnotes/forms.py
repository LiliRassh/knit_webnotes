from django import forms
from .models import Notes, Pattern, Tools, Yarn


class NotesForm(forms.ModelForm):
    project_name = forms.CharField(label='Название проекта')
    start_date = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Дата окончания', widget=forms.SelectDateWidget)
    for_who = forms.CharField(label='Для кого')
    craft = forms.CharField(label='Вид рукоделия')
    image = forms.FileField(label='Фото изделия')
    note = forms.CharField(label='Описание проекта', widget=forms.Textarea)
    # status = forms.ChoiceField(label='Статус', choices=((1, "В процессе"), (2, "Завершенный"),
    #                                                     (3, "Планируемый"), (4, "На паузе")))

    class Meta:
        model = Notes
        fields = ('project_name', 'start_date', 'end_date', 'for_who', 'craft', 'image', 'note', 'status')


class NotesForm2(forms.ModelForm):
    project_name = forms.CharField(label='Название проекта')
    start_date = forms.DateField(label='Дата начала', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='Дата окончания', widget=forms.SelectDateWidget)
    for_who = forms.CharField(label='Для кого')
    craft = forms.CharField(label='Вид рукоделия')
    note = forms.CharField(label='Описание проекта', widget=forms.Textarea)

    class Meta:
        model = Notes
        fields = ('project_name', 'start_date', 'end_date', 'for_who', 'craft', 'note', 'status')


class ToolsForm(forms.ModelForm):
    class Meta:
        model = Tools
        fields = ('type', 'producer', 'material', 'size', 'notes')


class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = ('name', 'image', 'scheme', 'description', 'source')


class YarnForm(forms.ModelForm):
    class Meta:
        model = Yarn
        fields = ('name', 'color_lot', 'weight', 'length', 'label', 'source')
