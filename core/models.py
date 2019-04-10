from django.db import models

# Create your models here.


class Provider(models.Model):

    name = models.CharField(verbose_name='Nome do fornecedor', max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
