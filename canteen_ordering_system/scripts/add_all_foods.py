import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_ordering_sys.settings')
django.setup()

from canteen.models import FoodItem

products = {
    "Beverages": ["Water", "Soda", "Natural juice", "Boxed juice", "Coconut water", "Iced tea"],
    "Savory items": ["Coxinha", "Fried pastry", "Baked pastry", "Ham and cheese roll", "Cheese bread", "Empanada", "Esfiha"],
    "Quick snacks": ["Natural sandwich", "Misto quente", "Simple burger", "Hot dog", "Tapioca", "Pizza slice"],
    "Sweets": ["Brigadeiro", "Beijinho", "Simple cake", "Filled cake", "Gelatin", "Donuts", "Cookies"],
    "Packaged snacks": ["Chips", "Peanuts", "Cereal bar", "Chocolate", "Candy", "Gum"],
    "Healthy products": ["Fresh fruits", "Yogurt", "Fruit salad", "Light wrap", "Nuts mix"],
    "Preparation items": ["Napkins", "Disposable cups", "Disposable plates", "Straws", "Snack bags", "Disposable gloves", "Paper towels", "Cleaning products"],
    "Basic ingredients": ["Bread", "French bread", "Cold cuts", "Sauces", "Pastry dough", "Flour and oil", "Sugar and milk", "Chicken", "Ground meat"],
    "Extra beverages": ["Coffee", "Cappuccino", "Hot chocolate", "Smoothies", "Zero soda", "Energy drink"],
    "Extra savory": ["Kibe", "Pastries", "Mini pizzas", "Meat balls", "Savory croissant"],
    "Extra sweets": ["Pudding", "Mousse", "Brownie", "Truffle"],
    "Useful snacks": ["Popcorn", "Toasts", "Cookies"],
    "Quick sale items": ["Ready meal", "Whole snacks", "Greek yogurt", "Portioned cheese"],
    "Non-food items": ["Reusable straws", "Water bottle", "Pre-paid cards", "Packaged napkins"],
    "Hygiene items": ["Wet wipes", "Alcohol gel", "Biodegradable bags"],
}

prices = {
    "Beverages": 5.00,
    "Savory items": 6.00,
    "Quick snacks": 12.00,
    "Sweets": 4.50,
    "Packaged snacks": 3.00,
    "Healthy products": 8.00,
    "Preparation items": 2.00,
    "Basic ingredients": 15.00,
    "Extra beverages": 6.50,
    "Extra savory": 7.00,
    "Extra sweets": 5.50,
    "Useful snacks": 3.50,
    "Quick sale items": 10.00,
    "Non-food items": 4.00,
    "Hygiene items": 5.00,
}

def populate_foods():
    total_added = 0
    total_skipped = 0
    
    for category, items in products.items():
        price = prices.get(category, 10.00)
        print(f"\nCategory: {category} (R$ {price:.2f})")
        
        for item_name in items:
            if FoodItem.objects.filter(name=item_name).exists():
                print(f"  SKIP: {item_name}")
                total_skipped += 1
                continue
            
            food = FoodItem.objects.create(
                name=item_name,
                description=f"Item from {category} category",
                price=int(price),
            )
            print(f"  ADD: {item_name}")
            total_added += 1
    
    print(f"\n{'='*50}")
    print(f"Added: {total_added} products")
    print(f"Skipped: {total_skipped} products")
    print(f"Categories: {len(products)}")
    print(f"{'='*50}")

if __name__ == "__main__":
    print("Starting food population...")
    populate_foods()
    print("Done!")
