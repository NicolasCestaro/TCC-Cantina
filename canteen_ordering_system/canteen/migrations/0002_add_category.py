# Generated migration

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='category',
            field=models.CharField(
                choices=[
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
                ],
                default='Lanches Rápidos',
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='food_pic'),
        ),
    ]
