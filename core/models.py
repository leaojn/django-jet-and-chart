from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class State (models.Model):
    state_acronym =  models.CharField(verbose_name='Sigla', max_length=2)
    name =  models.CharField(verbose_name='Nome', max_length=50)

class City (models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    state =  models.ForeignKey(verbose_name='Estado', related_name='state', on_delete=models.CASCADE)

class Contact (models.Model):
    description =  models.CharField(max_length=100)
    value = models.CharField(max_length=200)

class Provider(models.Model):

    TYPE_PROVIDER = (
        ('F', 'Física'),
        ('J', 'Jurídica')
    )

    name = models.CharField(verbose_name='Nome do fornecedor', max_length=100)
    type =  models.CharField(verbose_name='Tipo de fornecedor', max_length=1, choices=TYPE_PROVIDER)
    cpfCnpj = models.CharField(max_length=14)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    andress = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    contact = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name


class ProductCategory (models.Model):
    description = models.CharField(verbose_name='Categoria', max_length=100)


class Product(models.Model):
    description =  models.CharField(verbose_name='Nome do produto', max_length=100)
    bar_code = models.CharField(verbose_name='Código de Barras', max_length=100)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand = models.CharField(verbose_name='Marca', max_length=50)


class Input(models.Model):
    date_input =  models.DateTimeField(auto_created=True)
    provider =  models.ForeignKey(Provider, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User)
    products =  models.ManyToManyField(Product, through='ProductInput', through_fields=('product', 'input'),)


class ProductInput(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    input = models.ForeignKey(Input, on_delete=models.CASCADE)
    value = models.FloatField()
    quantity = models.IntegerField()