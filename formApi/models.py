from django.db import models

# Create your models here.


class Student(models.Model):
    roll = models.BigAutoField(verbose_name="Roll number", primary_key=True)
    name = models.CharField(max_length=255)
    admitted = models.BooleanField()
    birthday = models.DateField()
    age = models.DecimalField(max_digits=2, decimal_places=1)
    email = models.EmailField()
    about = models.TextField(verbose_name="About your self")
    website = models.URLField()
