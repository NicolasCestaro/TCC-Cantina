import os
import django
import sys

# Configurar o ambiente Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_ordering_sys.settings')
django.setup()

from canteen.models import FoodItem

def populate_foods():
    # Lista de itens do cardápio - apenas com dados essenciais
    foods = [
        {
            'name': 'Coxinha',
            'price': 5,
            'description': 'Coxinha de frango tradicional'
        },
        {
            'name': 'Biscoito de Polvilho',
            'price': 3,
            'description': 'Pacote de biscoito de polvilho crocante'
        },
        {
            'name': 'Pastel de Carne',
            'price': 6,
            'description': 'Pastel recheado com carne moída temperada'
        },
        {
            'name': 'Pastel de Queijo',
            'price': 6,
            'description': 'Pastel recheado com queijo derretido'
        },
        {
            'name': 'Suco de Laranja',
            'price': 4,
            'description': 'Copo 300ml de suco natural de laranja'
        },
        {
            'name': 'Suco de Uva',
            'price': 4,
            'description': 'Copo 300ml de suco de uva'
        },
        {
            'name': 'Suco de Limão',
            'price': 4,
            'description': 'Copo 300ml de suco natural de limão'
        },
        {
            'name': 'Halls',
            'price': 2,
            'description': 'Bala Halls - diversas cores'
        },
        {
            'name': 'Pirulito',
            'price': 1,
            'description': 'Pirulito diversos sabores'
        },
        {
            'name': 'Torrone',
            'price': 3,
            'description': 'Torrone de amendoim'
        },
        {
            'name': 'Bombom',
            'price': 2,
            'description': 'Bombom sortido'
        },
        {
            'name': 'Salgado de Calabresa',
            'price': 5,
            'description': 'Salgado assado recheado com calabresa e queijo'
        },
        {
            'name': 'Salgado de Salsicha',
            'price': 5,
            'description': 'Salgado assado recheado com salsicha'
        },
        {
            'name': 'Cachorro Quente',
            'price': 7,
            'description': 'Cachorro quente completo com salsicha, molho, batata palha e milho'
        },
        {
            'name': 'Esfirra',
            'price': 5,
            'description': 'Esfirra assada de carne'
        },
        {
            'name': 'Mini Pizza',
            'price': 6,
            'description': 'Mini pizza de mussarela com molho de tomate'
        },
        {
            'name': 'Hamburger',
            'price': 8,
            'description': 'Hambúrguer simples com alface, tomate e molho'
        },
        {
            'name': 'Refrigerante',
            'price': 5,
            'description': 'Lata 350ml (Coca-Cola, Guaraná ou Sprite)'
        }
    ]

    # Adicionar cada item ao banco de dados
    for food in foods:
        # Verificar se o item já existe
        if not FoodItem.objects.filter(name=food['name']).exists():
            try:
                food_item = FoodItem.objects.create(
                    name=food['name'],
                    price=food['price'],
                    description=food['description']
                )
                print(f"Adicionado: {food['name']}")
            except Exception as e:
                print(f"Erro ao adicionar {food['name']}: {str(e)}")
        else:
            print(f"{food['name']} já existe no banco de dados")

if __name__ == '__main__':
    print("Iniciando população do cardápio...")
    populate_foods()
    print("Processo finalizado!")