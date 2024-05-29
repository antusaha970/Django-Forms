# Generated by Django 5.0.6 on 2024-05-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Roll number')),
                ('name', models.CharField(max_length=255)),
                ('admitted', models.BooleanField()),
                ('birthday', models.DateField()),
                ('age', models.DecimalField(decimal_places=1, max_digits=2)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField(verbose_name='About your self')),
                ('website', models.URLField()),
            ],
        ),
    ]
