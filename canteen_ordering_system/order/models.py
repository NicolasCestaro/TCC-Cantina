from django.db import models
from django.contrib.auth.models import User
from canteen.models import FoodItem

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True, unique=True, verbose_name='CPF')
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
        
# Create your models here.
class Cart(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Accepted", "Accepted"),
    ("Cooking", "Cooking"),
    ("Packed", "Packed"),
    ("Completed", "Completed")
)

PAYMENT_CHOICES = (
    ("Cash", "Cash"),
    ("Online", "Online")
)

class Orders(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    order_datetime = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    transaction_id = models.CharField(max_length=100)
    payment_gateway = models.CharField(max_length=50)

class OrderItems(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE) 
    order = models.ForeignKey("Orders", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    item_total = models.IntegerField()