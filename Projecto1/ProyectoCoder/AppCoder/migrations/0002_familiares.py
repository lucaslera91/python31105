# Generated by Django 4.1 on 2022-09-02 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateField()),
                ('edad', models.IntegerField()),
            ],
        ),
    ]
