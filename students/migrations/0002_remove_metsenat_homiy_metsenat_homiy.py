# Generated by Django 4.0.6 on 2022-07-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metsenat',
            name='homiy',
        ),
        migrations.AddField(
            model_name='metsenat',
            name='homiy',
            field=models.ManyToManyField(blank=True, null=True, to='blog.sponsor'),
        ),
    ]
