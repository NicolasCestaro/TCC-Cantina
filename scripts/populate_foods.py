from decimal import Decimal
try:
    from canteen.models import FoodItem as Food
except Exception as e:
    print("Erro ao importar FoodItem:", e)
    raise SystemExit

products = [
  ('Coxinha', '5.00'),
  ('Pastel de queijo', '6.00'),
  ('Kibe frito', '5.50'),
  ('Enroladinho de salsicha', '4.50'),
  ('Pão de queijo (unidade)', '3.50'),
  ('Hambúrguer simples', '8.00'),
  ('Misto quente', '7.00'),
  ('Sanduíche natural', '9.50'),
  ('Batata frita pequena', '6.00'),
  ('Batata frita média', '9.00'),
  ('Brigadeiro', '2.50'),
  ('Beijinho', '2.50'),
  ('Bolo (fatia)', '5.00'),
  ('Cookie', '3.00'),
  ('Salgadinho (pacote)', '3.50'),
  ('Chips (pacote)', '4.00'),
  ('Refrigerante lata (350ml)', '5.00'),
  ('Refrigerante 600ml', '7.00'),
  ('Suco natural 300ml', '6.00'),
  ('Suco de caixinha', '3.00'),
  ('Água 500ml', '2.50'),
  ('Iogurte 170g', '3.50'),
]

for name, price in products:
    defaults = {}
    field_names = [f.name for f in Food._meta.fields]
    if 'price' in field_names:
        defaults['price'] = Decimal(price)
    elif 'valor' in field_names:
        defaults['valor'] = Decimal(price)
    obj, created = Food.objects.get_or_create(name=name, defaults=defaults)
    if not created:
        if 'price' in defaults:
            obj.price = defaults['price']
        elif 'valor' in defaults:
            obj.valor = defaults['valor']
        obj.save()
    print(('Created' if created else 'Updated'), name)

print("Pronto. Use exit() para sair.")