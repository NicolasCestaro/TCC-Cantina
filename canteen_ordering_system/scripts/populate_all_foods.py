import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_ordering_sys.settings')
django.setup()

from order.models import FoodItem

# Dados dos produtos organizados por categoria
products = {
    "Bebidas": [
        "Água mineral",
        "Refrigerante",
        "Suco natural",
        "Suco de caixinha",
        "Água de coco",
        "Chá gelado",
    ],
    "Salgados": [
        "Coxinha",
        "Pastel assado",
        "Pastel frito",
        "Enroladinho de presunto e queijo",
        "Pão de queijo",
        "Empada",
        "Esfiha",
    ],
    "Lanches rápidos": [
        "Sanduíche natural",
        "Misto quente",
        "Hambúrguer simples",
        "Cachorro quente",
        "Tapioca",
        "Pizza em pedaço",
    ],
    "Doces": [
        "Brigadeiro",
        "Beijinho",
        "Bolo simples",
        "Bolo recheado",
        "Gelatina",
        "Donuts",
        "Cookies",
    ],
    "Snacks embalados": [
        "Salgadinho tipo chips",
        "Amendoim",
        "Barrinha de cereal",
        "Chocolate",
        "Balas",
        "Chiclete",
    ],
    "Produtos saudáveis": [
        "Frutas lavadas (maçã, banana, uva)",
        "Iogurte",
        "Salada de frutas",
        "Wrap leve",
        "Mix de castanhas",
    ],
    "Itens de preparo e venda": [
        "Guardanapos",
        "Copos descartáveis",
        "Pratos descartáveis",
        "Canudos",
        "Saquinhos para lanche",
        "Luvas descartáveis",
        "Papel toalha",
        "Produtos de limpeza (álcool, detergente, esponja, pano)",
    ],
    "Ingredientes básicos": [
        "Pão de forma",
        "Pão francês",
        "Frios (presunto, queijo)",
        "Molhos (maionese, ketchup, mostarda)",
        "Massa de pastel",
        "Farinha, óleo, temperos básicos",
        "Açúcar, achocolatado, leite",
        "Frango",
        "Carne moída",
    ],
    "Bebidas extras": [
        "Café",
        "Cappuccino",
        "Achocolatado quente",
        "Vitaminas batidas",
        "Refrigerante zero",
        "Energético",
    ],
    "Salgados extras": [
        "Kibe",
        "Folhados variados",
        "Mini pizzas",
        "Bolinho de carne ou de queijo",
        "Croissant salgado",
    ],
    "Doces extras": [
        "Pudim",
        "Mousse",
        "Brownie",
        "Trufa",
    ],
    "Snacks úteis": [
        "Pipoca doce e salgada",
        "Torradas",
        "Biscoitos recheados e água e sal",
    ],
    "Produtos para venda rápida": [
        "Marmita pronta",
        "Salgados integrais",
        "Iogurte grego",
        "Queijo e presunto embalados em porções",
    ],
    "Itens sem ser comida": [
        "Canudos reutilizáveis",
        "Garrafinha de água tipo squeeze",
        "Cartela de fichas ou cartões pré-pagos",
        "Guardanapos e talheres embalados",
    ],
    "Higiene e apoio": [
        "Toalha umedecida",
        "Álcool em gel",
        "Sacolinhas biodegradáveis",
    ],
}

# Definir preços padrão por categoria
prices = {
    "Bebidas": 5.00,
    "Salgados": 6.00,
    "Lanches rápidos": 12.00,
    "Doces": 4.50,
    "Snacks embalados": 3.00,
    "Produtos saudáveis": 8.00,
    "Itens de preparo e venda": 2.00,
    "Ingredientes básicos": 15.00,
    "Bebidas extras": 6.50,
    "Salgados extras": 7.00,
    "Doces extras": 5.50,
    "Snacks úteis": 3.50,
    "Produtos para venda rápida": 10.00,
    "Itens sem ser comida": 4.00,
    "Higiene e apoio": 5.00,
}

def populate_foods():
    """Adiciona todos os produtos ao banco de dados"""
    total_added = 0
    total_skipped = 0
    
    for category, items in products.items():
        price = prices.get(category, 10.00)
        print(f"\n📂 Categoria: {category} (R$ {price:.2f})")
        
        for item_name in items:
            # Verificar se o item já existe
            if FoodItem.objects.filter(name=item_name).exists():
                print(f"   ⏭️  {item_name} - já existe, pulando...")
                total_skipped += 1
                continue
            
            # Criar novo item
            food = FoodItem.objects.create(
                name=item_name,
                description=f"Delicioso item da categoria {category}",
                price=price,
                category=category,
            )
            print(f"   ✅ {item_name} - adicionado com sucesso!")
            total_added += 1
    
    print(f"\n" + "="*50)
    print(f"✨ Resumo:")
    print(f"   • Produtos adicionados: {total_added}")
    print(f"   • Produtos já existentes: {total_skipped}")
    print(f"   • Total de categorias: {len(products)}")
    print(f"="*50)

if __name__ == "__main__":
    print("🍽️  Iniciando população do cardápio completo...")
    populate_foods()
    print("✅ Concluído!")
