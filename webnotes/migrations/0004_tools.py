# Generated by Django 3.0.6 on 2020-05-15 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webnotes', '0003_notes_status_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('producer', models.CharField(max_length=100, null=True)),
                ('material', models.CharField(max_length=100, null=True)),
                ('size', models.FloatField()),
                ('notes_id', models.ManyToManyField(to='webnotes.Notes')),
            ],
        ),
    ]
