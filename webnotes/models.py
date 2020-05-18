from django.db import models
from time import strftime


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.name


class Notes(models.Model):
    project_name = models.CharField(max_length=100, null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    create_date = models.DateTimeField(null=False, default=strftime('%Y-%m-%d %H:%M:%S'))
    for_who = models.CharField(max_length=100, null=False)
    craft = models.CharField(max_length=100, null=False)
    image = models.FileField(null=True, upload_to='upload/')
    note = models.TextField(max_length=512, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.project_name


class Tools(models.Model):
    type = models.CharField(max_length=100, null=False)
    producer = models.CharField(max_length=100, null=True)
    material = models.CharField(max_length=100, null=True)
    size = models.FloatField(null=False)
    notes = models.ManyToManyField(Notes)


class Yarn(models.Model):
    name = models.CharField(max_length=100, null=False)
    color_lot = models.CharField(max_length=100, null=False)
    weight = models.IntegerField(null=True)
    length = models.IntegerField(null=True)
    label = models.FileField(null=True, upload_to='upload/')
    source = models.URLField(null=True)
    notes = models.ManyToManyField(Notes)


class Pattern(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    image = models.FileField(null=True, upload_to='upload/')
    scheme = models.FileField(null=False, upload_to='upload/')
    description = models.TextField(max_length=1024)
    source = models.URLField(null=True)
    notes = models.ManyToManyField(Notes)

