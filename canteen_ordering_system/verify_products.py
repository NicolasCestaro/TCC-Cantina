#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_ordering_sys.settings')
django.setup()

from canteen.models import FoodItem
from django.db.models import Count

result = FoodItem.objects.values('category').annotate(total=Count('id')).order_by('-total')

print('=' * 60)
print('📊 PRODUTOS POR CATEGORIA')
print('=' * 60)

for cat in result:
    print(f'  {cat["category"]}: {cat["total"]} produtos')

total = FoodItem.objects.count()
print('=' * 60)
print(f'✅ TOTAL: {total} produtos no banco')
print('=' * 60)
