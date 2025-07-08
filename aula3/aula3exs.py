# Ex 1

product_list = [
    {'name': 'Teclado Mecânico', 'price': 350.00, 'in_stock': True},
    {'name': 'Mouse Gamer', 'price': 120.50, 'in_stock': False},
    {'name': 'Monitor 4K', 'price': 1800.00, 'in_stock': True},
    {'name': 'Webcam Full HD', 'price': 450.00, 'in_stock': True},
    {'name': 'Headset Pro', 'price': 550.00, 'in_stock': True}
]
for i in range(len(product_list)):

    if product_list[i]['price'] < 500 and product_list[i]['in_stock'] == True:
        print(f"\nNome : {product_list[i]['name']}")
        print(f"Preço : {product_list[i]['price']}\n")
        

for p in product_list:
    if p['price'] < 500 and p['in_stock'] == True:
        print(f"\n{p['name']}") 
        print(f"{p['price']}\n")

# Ex 2

post_slugs = ['como-aprender-django', 'guia-de-python-para-iniciantes', 'otimizando-queries-sql']

# Lista vazia para armazenar as URLs completas
full_urls = []



for i in range(len(post_slugs)):
    full_urls.append("/blog/" + post_slugs[i] + "/")

print(full_urls)

# Ex 3 

# Lista de nomes de tags
tag_names = ['Python', 'Django', 'Desenvolvimento Web', 'Banco de Dados']
    
# Lista vazia para as choices do formulário
form_choices = []

for i in range(len(tag_names)):
    form_choices.append((tag_names[i], tag_names[i]))

for i in range(len(form_choices)):
    print(f"\n{form_choices[i]}\n")

print(form_choices)



# Ex 4

users_to_deactivate = [
    {'username': 'ana.souza', 'email': 'ana@example.com', 'is_active': True},
    {'username': 'bruno.lima', 'email': 'bruno@example.com', 'is_active': True},
    {'username': 'carla.reis', 'email': 'carla@example.com', 'is_active': True}
]


for i in range(len(users_to_deactivate)):
    users_to_deactivate[i]['is_active'] = False
    print(f"Username : {users_to_deactivate[i]['username']}")
    print(f"Esta Ativo? : {users_to_deactivate[i]['is_active']}")


print(f"\n{users_to_deactivate}")




# Ex 5 


cart_items = [
    {'product': 'Cadeira Gamer', 'price': 1200.00, 'quantity': 1},
    {'product': 'Mousepad', 'price': 80.00, 'quantity': 2},
    {'product': 'Cabo USB-C', 'price': 50.00, 'quantity': 3}
]
total_price = 0.0

for i in range(len(cart_items)):

    total_price += cart_items[i]['price'] * cart_items[i]['quantity']

print(f"O valor total do carrinho é: R$ {total_price:.2f}")