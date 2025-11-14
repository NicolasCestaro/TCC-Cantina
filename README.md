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

### 1. Clonar Repositório
```bash
git clone https://github.com/NicolasCestaro/TCC-Cantina.git
cd TCC-Cantina/canteen_ordering_system
```

### 2. Criar Ambiente Virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar Migrações
```bash
python manage.py migrate
```

### 5. Carregar Dados Iniciais (Produtos)
```bash
python scripts/populate_all_foods.py
```

Isso carrega ~83 produtos em 15 categorias.

### 6. (Opcional) Criar Superusuário
```bash
python manage.py createsuperuser
```

Você será solicitado a inserir:
- Nome de usuário
- Email
- Senha

### 7. Iniciar Servidor de Desenvolvimento
```bash
python manage.py runserver
```

Abra seu navegador em: **http://127.0.0.1:8000**

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

**Última atualização:** Novembro 2025

Feito com ❤️ usando Django