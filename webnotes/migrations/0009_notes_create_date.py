# Generated by Django 3.0.6 on 2020-05-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webnotes', '0008_auto_20200516_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='create_date',
            field=models.DateTimeField(default='2020-05-16 20:48:56'),
        ),
    ]
