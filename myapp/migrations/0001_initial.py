# Generated by Django 4.2.1 on 2023-05-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searche', models.CharField(max_length=345)),
                ('createdon', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
