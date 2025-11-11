import os
import django
import sys

# Configurar o ambiente Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_ordering_sys.settings')
django.setup()

from canteen.models import FoodItem

def delete_foods():
    # Lista de produtos para deletar
    products_to_delete = ['X-Burger', 'Batata Frita']
    
    for product_name in products_to_delete:
        try:
            item = FoodItem.objects.get(name=product_name)
            item.delete()
            print(f"Produto '{product_name}' foi deletado com sucesso!")
        except FoodItem.DoesNotExist:
            print(f"Produto '{product_name}' não encontrado.")
        except Exception as e:
            print(f"Erro ao deletar '{product_name}': {str(e)}")

if __name__ == '__main__':
    print("\nDeletando produtos...")
    delete_foods()
    print("\nProdutos restantes:")
    print("-" * 50)
    for food in FoodItem.objects.all():
        print(f"ID: {food.id} - Nome: {food.name} - Preço: R${food.price}")
    print("-" * 50)