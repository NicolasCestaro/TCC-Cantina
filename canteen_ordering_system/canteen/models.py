from django.db import models

# Create your models here.

class FoodItem(models.Model):
    CATEGORY_CHOICES = (
        ('Bebidas', 'Bebidas'),
        ('Bebidas Extras', 'Bebidas Extras'),
        ('Salgados', 'Salgados'),
        ('Salgados Extras', 'Salgados Extras'),
        ('Lanches Rápidos', 'Lanches Rápidos'),
        ('Doces', 'Doces'),
        ('Snacks Embalados', 'Snacks Embalados'),
        ('Produtos Saudáveis', 'Produtos Saudáveis'),
        ('Itens de Preparo', 'Itens de Preparo'),
        ('Ingredientes Básicos', 'Ingredientes Básicos'),
        ('Snacks Úteis', 'Snacks Úteis'),
        ('Produtos para Venda Rápida', 'Produtos para Venda Rápida'),
        ('Itens Sem Ser Comida', 'Itens Sem Ser Comida'),
        ('Higiene e Apoio', 'Higiene e Apoio'),
    )
    
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='food_pic', blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Lanches Rápidos')

    def __str__(self):
        return self.name

