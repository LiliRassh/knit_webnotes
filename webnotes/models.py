from django.db import models
from time import strftime
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name


class Craft(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=100, null=False)
    size = models.FloatField(null=False)
    producer = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    material = models.CharField(max_length=100, null=True, blank=True)
    # webnote = models.ManyToManyField(Webnote)

    def __str__(self):
        return f'{self.name}: {self.size}мм - {self.producer}'


class Pattern(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    image = models.FileField(null=True, upload_to='upload/patterns/image', blank=True)
    scheme = models.FileField(null=True, upload_to='upload/patterns/scheme', blank=True)
    description = models.TextField(max_length=1024)
    source = models.URLField(null=True, blank=True)
    # webnote = models.ManyToManyField(Webnote)

    def __str__(self):
        return self.name


class Yarn(models.Model):
    name = models.CharField(max_length=100, null=False)
    color_lot = models.CharField(max_length=100, null=False)
    weight = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    label = models.FileField(null=True, upload_to='upload/yarns', blank=True)
    source = models.URLField(null=True, blank=True)
    # webnote = models.ManyToManyField(Webnote, verbose_name='Проект')

    def __str__(self):
        return f'{self.name}:{self.color_lot}/{self.weight}гр-{self.length}м'


class Webnote(models.Model):
    project_name = models.CharField(max_length=100, null=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M:%S'))
    for_who = models.CharField(max_length=100, null=False)
    craft = models.ForeignKey(Craft, verbose_name='Вид рукоделия', on_delete=models.CASCADE, default=0)
    image = models.FileField(null=True, upload_to='upload/webnotes', blank=True)
    note = models.TextField(max_length=512, null=True, blank=True)
    private_status = models.CharField(max_length=100, null=False, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name='Статус', on_delete=models.CASCADE, default=0)
    tool = models.ManyToManyField(Tool, verbose_name='Инструменты')
    pattern = models.ManyToManyField(Pattern, verbose_name='Узор')
    yarn = models.ManyToManyField(Yarn, verbose_name='Пряжа')

    def __str__(self):
        return f'{self.project_name}-{self.for_who}: {self.craft}{self.status}/{self.private_status}'
