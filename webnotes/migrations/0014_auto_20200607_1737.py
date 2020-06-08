# Generated by Django 3.0.6 on 2020-06-07 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webnotes', '0013_auto_20200531_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='webnote',
            name='private_status',
        ),
        migrations.AlterField(
            model_name='webnote',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='webnote',
            name='tool',
            field=models.ManyToManyField(to='webnotes.Tool', verbose_name='Инструменты'),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='length',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yarn',
            name='weight',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='webnote',
            name='access',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='webnotes.Access', verbose_name='Доступ другим пользователям'),
        ),
    ]