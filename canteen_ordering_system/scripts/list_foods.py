import os
import django
import sys

# Configurar o ambiente Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_ordering_sys.settings')
django.setup()

from canteen.models import FoodItem

def list_foods():
    print("\nProdutos no cardápio:")
    print("-" * 50)
    for food in FoodItem.objects.all():
        print(f"ID: {food.id} - Nome: {food.name} - Preço: R${food.price}")
    print("-" * 50)

if __name__ == '__main__':
    list_foods()