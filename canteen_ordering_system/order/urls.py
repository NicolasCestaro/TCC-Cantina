from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('update-cart/<int:f_id>/', views.update_cart, name='update-cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('myorders/', views.my_orders, name='my-orders'),
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel-order'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='profile-edit'),
    path('sobre/', views.sobre, name='sobre'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)