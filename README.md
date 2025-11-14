# 🍽️ TCC-Cantina - Sistema de Pedidos Online para Cantina

Um sistema web completo de gerenciamento e pedidos para cantinas, desenvolvido com **Django** e **Bootstrap**. Permite que usuários façam pedidos de produtos, gerenciem seu carrinho de compras e acompanhem o status de seus pedidos em tempo real.

---

## ✨ Características Principais

### 👥 Para Clientes
- **Autenticação e Registro** - Cadastro seguro com validação de CPF
- **Cardápio Interativo** - Visualize produtos organizados por categorias (Bebidas, Salgados, Lanches, Doces, etc.)
- **Carrinho de Compras** - Adicione, edite quantidades e remova itens
- **Checkout Flexível** - Pagamento em dinheiro ou online (PayPal)
- **Histórico de Pedidos** - Acompanhe todos os seus pedidos com status em tempo real
- **Perfil do Usuário** - Edite dados pessoais (telefone, endereço, foto de perfil, CPF)
- **Avaliação de Produtos** - Visualize ratings de cada produto
- **Sistema de Cancelamento** - Cancele pedidos em fase Pendente ou Aceito

### 🛠️ Para Administradores
- **Painel Django Admin** - Gerenciamento completo de produtos, pedidos e usuários
- **Gestão de Categorias** - Organize produtos em 14 categorias distintas
- **Controle de Status de Pedidos** - Atualize status: Pendente → Aceito → Preparando → Empacotado → Concluído
- **Banco de Dados Seguro** - SQLite com migrations automáticas

### 🎨 Interface Moderna
- Design responsivo com **Bootstrap 5**
- Gradient moderno com azul e cores vibrantes
- Ícones FontAwesome para melhor UX
- Completamente funcional em celular, tablet e desktop
- Grid de produtos em colunas (1-3 colunas conforme resolução)

---

## 🏗️ Arquitetura do Projeto

```
TCC-Cantina/
├── canteen_ordering_system/          # Projeto Django principal
│   ├── manage.py                     # Utilitário de linha de comando Django
│   ├── db.sqlite3                    # Banco de dados SQLite
│   ├── requirements.txt              # Dependências Python
│   ├── canteen_ordering_sys/         # Configurações do projeto
│   │   ├── settings.py              # Configuração Django (BD, apps, middleware)
│   │   ├── urls.py                  # URLs principais do projeto
│   │   ├── wsgi.py                  # Configuração WSGI para produção
│   │   └── asgi.py                  # Configuração ASGI
│   ├── canteen/                     # App Django para Produtos (Cardápio)
│   │   ├── models.py                # Modelo FoodItem (produtos)
│   │   ├── admin.py                 # Painel admin para Produtos
│   │   ├── migrations/              # Histórico de alterações no BD
│   │   └── apps.py
│   ├── order/                       # App Django para Pedidos
│   │   ├── models.py                # Modelos: Cart, Orders, OrderItems, Profile
│   │   ├── views.py                 # Lógica de negócio (carrinho, checkout, perfil)
│   │   ├── forms.py                 # Formulários (registro, login, perfil)
│   │   ├── urls.py                  # URLs de order (menu, cart, checkout, etc)
│   │   ├── signals.py               # Sinais Django
│   │   ├── validators.py            # Validadores customizados
│   │   ├── templates/order/         # Templates HTML
│   │   │   ├── menu.html            # Cardápio com grid de produtos
│   │   │   ├── cart.html            # Carrinho de compras
│   │   │   ├── checkout.html        # Página de checkout
│   │   │   ├── myorders.html        # Histórico de pedidos
│   │   │   ├── profile.html         # Perfil do usuário
│   │   │   ├── index.html           # Página inicial
│   │   │   ├── login.html           # Login
│   │   │   ├── register.html        # Registro
│   │   │   ├── sobre.html           # Sobre
│   │   │   └── edit_profile_new.html # Edição de perfil
│   │   ├── templates/base/
│   │   │   └── base.html            # Template base com navbar
│   │   ├── templatetags/
│   │   │   └── rating_tags.py       # Tags customizadas para ratings
│   │   └── migrations/
│   ├── static/                      # CSS, JS, imagens estáticas
│   ├── media/                       # Uploads de usuários (fotos de perfil)
│   └── scripts/                     # Scripts auxiliares
│       ├── populate_all_foods.py    # Popula BD com ~83 produtos
│       ├── add_all_foods.py         # Adiciona mais produtos
│       ├── delete_foods.py          # Limpa produtos
│       └── inspect_db.py            # Inspeção de BD
├── scripts/                         # Scripts complementares
│   └── populate_foods.py            # Script simples de população
└── README.md                        # Este arquivo
```

---

## 🗄️ Modelos de Dados

### FoodItem (canteen/models.py)
Representa um produto no cardápio.

```python
- name: CharField (até 50 caracteres)
- price: IntegerField (preço em centavos)
- description: CharField (até 5000 caracteres)
- image: ImageField (opcional)
- category: CharField (14 categorias pré-definidas)
```

**Categorias disponíveis:**
- Bebidas, Bebidas Extras
- Salgados, Salgados Extras
- Lanches Rápidos
- Doces, Doces Extras
- Snacks Embalados, Snacks Úteis
- Produtos Saudáveis
- Itens de Preparo
- Ingredientes Básicos
- Produtos para Venda Rápida
- Itens Sem Ser Comida
- Higiene e Apoio

### Profile (order/models.py)
Extensão do usuário Django com informações adicionais.

```python
- user: OneToOneField (Django User)
- profile_pic: ImageField (foto de perfil)
- cpf: CharField (único, validado)
- phone_number: CharField
- address: TextField
- created_at: DateTimeField
```

### Cart (order/models.py)
Representa itens no carrinho de um usuário.

```python
- username: ForeignKey (User)
- food: ForeignKey (FoodItem)
- quantity: PositiveIntegerField
```

### Orders (order/models.py)
Representa um pedido finalizado.

```python
- username: ForeignKey (User)
- total_amount: IntegerField
- order_datetime: DateTimeField
- payment_mode: CharField (Cash ou Online)
- status: CharField (Pending, Accepted, Cooking, Packed, Completed)
- transaction_id: CharField
- payment_gateway: CharField (Cash ou Paypal)
```

### OrderItems (order/models.py)
Itens individuais dentro de um pedido.

```python
- username: ForeignKey (User)
- order: ForeignKey (Orders)
- name: CharField (nome do produto)
- price: IntegerField
- quantity: PositiveIntegerField
- item_total: IntegerField
```

---

## 🚀 Instalação e Setup

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)
- Git

---

## 📋 SETUP RÁPIDO - COMANDOS COMPLETOS (Windows PowerShell)

**Copie e execute TODOS esses comandos para configurar o projeto sem erros:**

### 1️⃣ Clone e entre na pasta do projeto
```powershell
git clone https://github.com/NicolasCestaro/TCC-Cantina.git
cd TCC-Cantina\canteen_ordering_system
```

### 2️⃣ Remova banco antigo (se existir) e crie novo ambiente virtual
```powershell
if (Test-Path .\db.sqlite3) { Remove-Item -Force .\db.sqlite3 }
python -m venv venv
```

### 3️⃣ Instale as dependências (Django 4.2 e Pillow)
```powershell
pip install -r requirements.txt
```

### 4️⃣ Execute as migrations para criar as tabelas no banco
```powershell
python manage.py showmigrations
python manage.py migrate
python manage.py showmigrations
```

**Saída esperada:** Todas as migrations devem ter um `[X]` marcando que foram aplicadas.

### 5️⃣ Popule o banco com 125 produtos
```powershell
python -c "
import os, sys, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canteen_ordering_sys.settings')
django.setup()
from decimal import Decimal
from canteen.models import FoodItem as Food
products = [
  ('Refrigerante lata (350ml)', '5.00', 'Bebidas'),
  ('Refrigerante 600ml', '7.00', 'Bebidas'),
  ('Guaraná lata (350ml)', '5.00', 'Bebidas'),
  ('Suco natural 300ml', '6.00', 'Bebidas'),
  ('Suco de caixinha', '3.00', 'Bebidas'),
  ('Água 500ml', '2.50', 'Bebidas'),
  ('Água 1.5L', '4.00', 'Bebidas'),
  ('Chá gelado', '4.50', 'Bebidas'),
  ('Achocolatado', '5.00', 'Bebidas'),
  ('Soda italiana', '6.00', 'Bebidas'),
  ('Limonada natural', '5.50', 'Bebidas'),
  ('Suco de laranja natural', '6.50', 'Bebidas'),
  ('Energético lata', '8.00', 'Bebidas'),
  ('Cerveja (350ml)', '6.00', 'Bebidas'),
  ('Vinho tinto (copo)', '12.00', 'Bebidas'),
  ('Café com leite', '4.00', 'Bebidas Extras'),
  ('Cappuccino', '7.00', 'Bebidas Extras'),
  ('Café expresso', '3.50', 'Bebidas Extras'),
  ('Café americano', '3.00', 'Bebidas Extras'),
  ('Chocolate quente', '5.50', 'Bebidas Extras'),
  ('Leite quente', '3.50', 'Bebidas Extras'),
  ('Chá quente variado', '3.00', 'Bebidas Extras'),
  ('Milkshake morango', '8.00', 'Bebidas Extras'),
  ('Milkshake chocolate', '8.00', 'Bebidas Extras'),
  ('Milkshake baunilha', '8.00', 'Bebidas Extras'),
  ('Coxinha', '5.00', 'Salgados'),
  ('Pastel de queijo', '6.00', 'Salgados'),
  ('Kibe frito', '5.50', 'Salgados'),
  ('Enroladinho de salsicha', '4.50', 'Salgados'),
  ('Pão de queijo (unidade)', '3.50', 'Salgados'),
  ('Empada', '5.00', 'Salgados'),
  ('Bola de carne', '4.50', 'Salgados'),
  ('Croissant de presunto', '6.50', 'Salgados'),
  ('Risole de carne', '5.00', 'Salgados'),
  ('Esfirra de carne', '5.50', 'Salgados'),
  ('Torta de frango', '7.00', 'Salgados'),
  ('Quiche de verdura', '7.50', 'Salgados'),
  ('Sequilho', '3.50', 'Salgados'),
  ('Biscoito de polvilho', '4.00', 'Salgados'),
  ('Bolacha salgada (pacote)', '3.00', 'Salgados'),
  ('Broa de chuchu', '5.00', 'Salgados'),
  ('Bolo de milho', '4.50', 'Salgados'),
  ('Acarajé', '6.00', 'Salgados'),
  ('Pastel de carne', '6.00', 'Salgados'),
  ('Pastéis doces variados', '5.50', 'Salgados'),
  ('Hambúrguer simples', '8.00', 'Salgados Extras'),
  ('Hambúrguer duplo', '12.00', 'Salgados Extras'),
  ('Misto quente', '7.00', 'Salgados Extras'),
  ('Sanduíche natural', '9.50', 'Salgados Extras'),
  ('Sanduíche de atum', '10.00', 'Salgados Extras'),
  ('Torta presunto e queijo', '8.00', 'Salgados Extras'),
  ('Cachorro quente', '6.00', 'Salgados Extras'),
  ('Cachorro quente completo', '8.00', 'Salgados Extras'),
  ('X-Burguer', '9.00', 'Salgados Extras'),
  ('X-Egg', '10.00', 'Salgados Extras'),
  ('X-Bacon', '11.00', 'Salgados Extras'),
  ('Frango empanado', '9.00', 'Salgados Extras'),
  ('Peixe empanado', '10.00', 'Salgados Extras'),
  ('Tira de frango', '8.50', 'Salgados Extras'),
  ('Batata frita grande', '12.00', 'Salgados Extras'),
  ('Batata frita pequena', '6.00', 'Lanches Rápidos'),
  ('Batata frita média', '9.00', 'Lanches Rápidos'),
  ('Batata frita com queijo', '10.00', 'Lanches Rápidos'),
  ('Batata frita com bacon', '11.00', 'Lanches Rápidos'),
  ('Aros de cebola', '7.00', 'Lanches Rápidos'),
  ('Nuggets (6 peças)', '8.00', 'Lanches Rápidos'),
  ('Asas de frango (4 peças)', '9.00', 'Lanches Rápidos'),
  ('Bolinhas de queijo', '7.50', 'Lanches Rápidos'),
  ('Pastel frito (unidade)', '5.50', 'Lanches Rápidos'),
  ('Pão na chapa', '4.00', 'Lanches Rápidos'),
  ('Tapioca simples', '5.00', 'Lanches Rápidos'),
  ('Tapioca com queijo', '6.50', 'Lanches Rápidos'),
  ('Brigadeiro', '2.50', 'Doces'),
  ('Beijinho', '2.50', 'Doces'),
  ('Romeu e Julieta', '3.00', 'Doces'),
  ('Bolo (fatia)', '5.00', 'Doces'),
  ('Bolo de chocolate (fatia)', '5.50', 'Doces'),
  ('Bolo de cenoura (fatia)', '5.00', 'Doces'),
  ('Pudim (unidade)', '4.00', 'Doces'),
  ('Mousse de chocolate', '6.00', 'Doces'),
  ('Pavê', '5.50', 'Doces'),
  ('Torta de frutas vermelhas', '7.00', 'Doces'),
  ('Sonho (unidade)', '4.50', 'Doces'),
  ('Churro', '3.50', 'Doces'),
  ('Churro com chocolate', '5.00', 'Doces'),
  ('Donut', '4.00', 'Doces'),
  ('Donut com cobertura', '5.00', 'Doces'),
  ('Brownie', '5.00', 'Doces'),
  ('Bolo de chocolate gelado', '6.00', 'Doces'),
  ('Sorvete (bola)', '4.00', 'Doces'),
  ('Chips (pacote)', '4.00', 'Snacks Embalados'),
  ('Salgadinho (pacote)', '3.50', 'Snacks Embalados'),
  ('Pirulito', '1.50', 'Snacks Embalados'),
  ('Chiclete', '1.00', 'Snacks Embalados'),
  ('Bala', '0.50', 'Snacks Embalados'),
  ('Chocolate', '3.00', 'Snacks Embalados'),
  ('Chocolate branco', '3.00', 'Snacks Embalados'),
  ('Biscoito doce (pacote)', '3.50', 'Snacks Embalados'),
  ('Biscoito recheado (pacote)', '4.00', 'Snacks Embalados'),
  ('Rosca doce', '3.00', 'Snacks Embalados'),
  ('Amendoim (pacote)', '4.50', 'Snacks Embalados'),
  ('Castanha (pacote)', '6.00', 'Snacks Embalados'),
  ('Mix de castanhas', '7.00', 'Snacks Embalados'),
  ('Pipoca (pacote)', '3.00', 'Snacks Embalados'),
  ('Granola (pacote)', '5.00', 'Snacks Embalados'),
  ('Iogurte 170g', '3.50', 'Bebidas'),
  ('Iogurte grego 150g', '5.00', 'Bebidas'),
  ('Iogurte com granola', '6.00', 'Bebidas'),
  ('Fruta da estação (pote)', '7.00', 'Produtos Saudáveis'),
  ('Salada verde (pote)', '8.00', 'Produtos Saudáveis'),
  ('Salada caesar (pote)', '9.00', 'Produtos Saudáveis'),
  ('Açai 300ml', '10.00', 'Produtos Saudáveis'),
  ('Smoothie morango', '8.50', 'Bebidas Extras'),
  ('Smoothie banana', '8.50', 'Bebidas Extras'),
  ('Smoothie detox', '9.00', 'Bebidas Extras'),
  ('Mel (pote pequeno)', '5.00', 'Ingredientes Básicos'),
  ('Geleia (pote pequeno)', '4.00', 'Ingredientes Básicos'),
  ('Manteiga (pote)', '6.00', 'Ingredientes Básicos'),
  ('Cream cheese (pote)', '7.00', 'Ingredientes Básicos'),
  ('Queijo ralado (pote)', '5.50', 'Ingredientes Básicos'),
  ('Azeite (frasco)', '8.00', 'Ingredientes Básicos'),
  ('Molho de tomate (frasco)', '4.50', 'Ingredientes Básicos'),
  ('Maionese (pote)', '5.00', 'Ingredientes Básicos'),
  ('Catchup (frasco)', '4.00', 'Ingredientes Básicos'),
]
for name, price, category in products:
    defaults = {'price': int(float(price) * 100), 'category': category}
    Food.objects.get_or_create(name=name, defaults=defaults)
print(f'✅ {Food.objects.count()} produtos carregados')
"
```

### 6️⃣ (Opcional) Criar Superusuário para acessar admin
```powershell
python manage.py createsuperuser
```

Você será solicitado a inserir:
- Nome de usuário
- Email
- Senha

### 7️⃣ Iniciar Servidor de Desenvolvimento
```powershell
python manage.py runserver
```

Abra seu navegador em: **http://127.0.0.1:8000**

**Sucesso! ✅ Acesse:**
- **Home:** http://127.0.0.1:8000/
- **Cardápio:** http://127.0.0.1:8000/menu/
- **Admin:** http://127.0.0.1:8000/admin/

---

## 🔗 URLs e Rotas Principais

| Rota | Descrição | Autenticação |
|------|-----------|--------------|
| `/` | Página inicial | Não |
| `/menu/` | Cardápio com produtos | Sim |
| `/register/` | Página de registro | Não |
| `/login/` | Página de login | Não |
| `/logout/` | Logout | Sim |
| `/cart/` | Carrinho de compras | Sim |
| `/checkout/` | Finalizar pedido | Sim |
| `/myorders/` | Histórico de pedidos | Sim |
| `/cancel-order/<id>/` | Cancelar pedido | Sim |
| `/profile/` | Visualizar perfil | Sim |
| `/profile/edit/` | Editar perfil | Sim |
| `/update-cart/<id>/` | Adicionar/remover itens | Sim |
| `/sobre/` | Página sobre | Não |
| `/admin/` | Painel administrativo | Admin |

---

## 💳 Sistema de Pagamento

### Opções Disponíveis
1. **Dinheiro (Cash)** - Pagamento no local
   - ID gerado automaticamente: `CASH` + 15 dígitos aleatórios
   
2. **PayPal** - Pagamento online
   - Integração com API PayPal
   - Requer configuração de credenciais

---

## 🔐 Segurança

- ✅ **CSRF Protection** - Ativado para todos os formulários
- ✅ **Password Hashing** - Senhas com hash PBKDF2
- ✅ **SQL Injection Prevention** - ORM Django protege queries
- ✅ **CPF Validation** - Validação de CPF com digito verificador
- ✅ **Session Management** - Sessões seguras com cookies HttpOnly
- ⚠️ **DEBUG = True** - Desative em produção!

### Checklist Produção
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['seu-dominio.com']
SECRET_KEY = 'gere uma nova chave secreta'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## 📊 Estatísticas do Projeto

- **83 Produtos** carregados inicialmente em 15 categorias
- **14 Templates** HTML customizados
- **5 Modelos** Django principais
- **Django 4.2** + **Bootstrap 5** + **FontAwesome Icons**
- **Responsivo** para mobile, tablet e desktop

---

## 🛠️ Scripts Úteis

### Carregar Todos os Produtos
```bash
python scripts/populate_all_foods.py
```

### Listar Produtos no BD
```bash
python scripts/list_foods.py
```

### Adicionar Mais Produtos
```bash
python scripts/add_all_foods.py
```

### Deletar Todos os Produtos
```bash
python scripts/delete_foods.py
```

### Inspecionar Banco de Dados
```bash
python scripts/inspect_db.py
```

---

## 🐛 Troubleshooting

### "No such table: auth_user"
**Solução:** Execute as migrações:
```bash
python manage.py migrate
```

### Imagens não aparecem
**Verificar:**
1. Arquivo foi salvo em `media/`
2. `MEDIA_URL` e `MEDIA_ROOT` configurados em `settings.py`
3. URL estática servida corretamente (desenvolvimento usa `runserver`)

### Erro ao registrar CPF duplicado
**Causa:** CPF já cadastrado no sistema (campo unique)
**Solução:** Use outro CPF ou delete o registro anterior em `/admin/`

### Servidor não inicia
**Verificar:**
1. Porta 8000 está disponível
2. Ambiente virtual ativado
3. Dependências instaladas: `pip install -r requirements.txt`

---

## 📝 Desenvolvimento Futuro

- [ ] Integração com PayPal completa
- [ ] Notificações via email para pedidos
- [ ] Painel de vendas para administradores
- [ ] Avaliações e comentários de clientes
- [ ] Sistema de cupons de desconto
- [ ] Dark mode
- [ ] Aplicativo mobile com React Native
- [ ] Cache de produtos
- [ ] Busca avançada e filtros
- [ ] Sistema de reviews com fotos

---

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é fornecido como está para fins educacionais (Trabalho de Conclusão de Curso).

---

## 👨‍💻 Autor

**Nicolás Cestaro**

- GitHub: [@NicolasCestaro](https://github.com/NicolasCestaro)

---

## 📞 Suporte

Para reportar bugs ou sugerir melhorias, abra uma [Issue](https://github.com/NicolasCestaro/TCC-Cantina/issues) no repositório.

---

## 🎯 Objetivo do Projeto

Este é um **Trabalho de Conclusão de Curso (TCC)** que visa desenvolver um sistema web prático e funcional para gerenciamento de pedidos em cantinas, demonstrando conhecimento em:

- ✅ Backend com Django
- ✅ Frontend responsivo com Bootstrap
- ✅ Banco de dados relacional (SQLite)
- ✅ Autenticação e autorização
- ✅ MVC/MVT architecture
- ✅ Boas práticas de desenvolvimento web

---

**Important (when cloning this repository)**

- If you cloned this repository and see "no such table: canteen_fooditem" or similar database errors, it means your local SQLite file is not in sync with migrations. To fix this on the machine you cloned to, run:

```powershell
# from the project folder containing manage.py
python -m venv venv; .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python scripts/populate_foods.py
python manage.py runserver
```

- If the repository contains a committed `db.sqlite3` (from another machine), it can cause schema mismatches. Remove the tracked DB (once) so others won't get the wrong DB:

```powershell
git rm --cached canteen_ordering_system\db.sqlite3
git commit -m "Remove committed SQLite DB; use migrations instead"
git push
```

This repository now includes a `.gitignore` that excludes `db.sqlite3` and `media/` so the local DB and uploads won't be committed again.


**Última atualização:** Novembro 2025

Feito com ❤️ usando Django