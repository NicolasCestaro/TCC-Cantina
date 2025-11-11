from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from canteen.models import FoodItem
from .models import Cart, Orders, OrderItems, Profile
from .forms import LoginRegisterForm, ProfileForm, CustomUserCreationForm
import random
from django.contrib.auth.forms import UserCreationForm

# Página inicial
def index(request):
    # Página inicial sem listar comidas
    return render(request, 'order/index.html', {})

# Registro
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Conta criada com sucesso! Por favor, faça login.")
            return redirect('login')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Login
def user_login(request):
    if request.method == 'GET':
        form = LoginRegisterForm()
        return render(request, 'order/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginRegisterForm(request.POST)
        un = request.POST.get('username')
        pw = request.POST.get('password')
        if not User.objects.filter(username=un).exists():
            messages.warning(request, 'User Does Not Exist or Wrong Password, Try Again')
            return HttpResponseRedirect('/login/')
        else:
            auth_user = authenticate(username=un, password=pw)
            if auth_user:
                login(request, auth_user)
                return HttpResponseRedirect('/')
            else:
                messages.warning(request, 'User Does Not Exist or Wrong Password, Try Again')
                return HttpResponseRedirect('/login/')

# Atualizar carrinho
@login_required(login_url='/login/')
def update_cart(request, f_id):
    food = FoodItem.objects.get(id=f_id)
    action = request.GET.get('name')
    
    if Cart.objects.filter(username=request.user, food=food).exists():
        old_quantity = Cart.objects.values_list('quantity', flat=True).get(username=request.user, food=food)
        if action == 'increase_cart':
            updated_quantity = old_quantity + 1
            Cart.objects.filter(username=request.user, food=food).update(quantity=updated_quantity)
            messages.success(request, f'Quantidade de {food.name} aumentada para {updated_quantity}')
        elif action == 'decrease_cart':
            updated_quantity = old_quantity - 1
            if updated_quantity <= 0:
                item_to_delete = Cart.objects.get(username=request.user, food=food)
                item_to_delete.delete()
                messages.info(request, f'{food.name} removido do carrinho')
            else:
                Cart.objects.filter(username=request.user, food=food).update(quantity=updated_quantity)
                messages.success(request, f'Quantidade de {food.name} diminuída para {updated_quantity}')
        elif action == 'delete_cart_item':
            item_to_delete = Cart.objects.get(username=request.user, food=food)
            item_to_delete.delete()
            messages.info(request, f'{food.name} removido do carrinho')
    else:
        cart_item = Cart(username=request.user, food=food)
        cart_item.save()
        messages.success(request, f'{food.name} adicionado ao carrinho')

    # Redirecionar de volta para a página anterior
    referer = request.META.get('HTTP_REFERER')
    if referer:
        if 'cart' in referer:
            return redirect('cart')
        elif 'menu' in referer:
            return redirect('menu')
    return redirect('menu')  # fallback para o menu
# Carrinho
@login_required(login_url='/login/')
def cart(request):
    cartitems = Cart.objects.filter(username=request.user)
    total_amount = 0
    if cartitems:
        for item in cartitems:
            sub_total = item.food.price * item.quantity
            total_amount += sub_total
    return render(request, 'order/cart.html', {'cartitems': cartitems, 'total_amount': total_amount})

# Checkout
@login_required(login_url='/login/')
def checkout(request):
    if request.method == 'POST':
        if request.POST.get('paymode') == 'Cash':
            tn_id = 'CASH' + str(random.randint(111111111111111, 999999999999999))
            payment_mode = "Cash"
            payment_gateway = "Cash"
        elif request.POST.get('paymode') == 'Online' and request.POST.get('paygate') == "Paypal":
            tn_id = request.POST.get('tn_id')
            payment_mode = "Online"
            payment_gateway = "Paypal"
        else:
            return HttpResponse('<H1>Invalid Request</H1>')
        cartitems = Cart.objects.filter(username=request.user)
        total_amount = 0
        new_order = Orders(username=request.user, total_amount=total_amount, payment_mode=payment_mode, transaction_id=tn_id, payment_gateway=payment_gateway)
        new_order.save()
        if cartitems:
            for item in cartitems:
                OrderItems(username=request.user, order=new_order, name=item.food.name, price=item.food.price, quantity=item.quantity, item_total=item.food.price * item.quantity).save()
                sub_total = item.food.price * item.quantity
                total_amount += sub_total
            Orders.objects.filter(id=new_order.id).update(total_amount=total_amount)
        cartitems.delete()
        return HttpResponseRedirect('/myorders/')
    else:
        return HttpResponse('<H1>Invalid Request</H1>')

# Meus pedidos
@login_required(login_url='/login/')
def my_orders(request):
    orders = Orders.objects.filter(username=request.user).order_by("-order_datetime", "id")
    # montar estrutura de itens por pedido incluindo tentativa de imagem via FoodItem
    order_list = []
    for order in orders:
        items_qs = OrderItems.objects.filter(order=order)
        items = []
        for it in items_qs:
            # tentar recuperar imagem da tabela FoodItem pelo nome (se existir)
            image_url = None
            try:
                fi = FoodItem.objects.filter(name__iexact=it.name).first()
                if fi and fi.image:
                    image_url = fi.image.url
            except Exception:
                image_url = None
            items.append({
                'id': it.id,
                'name': it.name,
                'price': it.price,
                'quantity': it.quantity,
                'item_total': it.item_total,
                'image_url': image_url,
            })
        order_list.append({
            'order': order,
            'items': items,
        })
    return render(request, 'order/myorders.html', {'orders': orders, 'order_list': order_list})


@login_required(login_url='/login/')
def cancel_order(request, order_id):
    """Permite cancelar um pedido do próprio usuário se ainda estiver em estado cancelável (Pending ou Accepted).
    Isso apenas marca como 'Cancelled' para histórico.
    """
    try:
        order = Orders.objects.get(id=order_id, username=request.user)
    except Orders.DoesNotExist:
        messages.error(request, 'Pedido não encontrado.')
        return redirect('my-orders')

    if order.status in ["Pending", "Accepted"]:
        order.status = 'Cancelled'
        order.save()
        messages.success(request, f'Pedido #{order.id} foi cancelado.')
    else:
        messages.warning(request, 'Este pedido não pode ser cancelado no momento.')
    return redirect('my-orders')

# Logout
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return HttpResponseRedirect('/')

# Menu
@login_required(login_url='/login/')
# Novo perfil
@login_required(login_url='/login/')
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    orders = Orders.objects.filter(username=request.user).order_by("-order_datetime", "id")
    return render(request, 'order/profile.html', {'orders': orders})
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    orders = getattr(request.user, 'orders', [])
    return render(request, 'order/profile.html', {'orders': orders})

@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'order/edit_profile_new.html', {'form': form, 'profile': profile})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from canteen.models import FoodItem

def index(request):
    # Página inicial sem listar comidas
    return render(request, 'order/index.html', {})

def menu(request):
    # Buscar todos os itens do cardápio ordenados por categoria
    foods = FoodItem.objects.all().order_by('category', 'name')
    return render(request, 'order/menu.html', {'foods': foods})

def sobre(request):
    """Página 'Sobre' simples."""
    return render(request, 'order/sobre.html')