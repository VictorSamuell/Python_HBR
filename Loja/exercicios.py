from Store.models import Cliente, Categoria, Produto, Pedido, ItemPedido
from django.db.models import Value, F, Sum

print("\n===============")
print("DJANGO")
print("===============")


# # Exercicio 1

ProPro = Produto.objects.all().order_by('preco')
for Pro in ProPro:
    print(f"{Pro.nome}, {Pro.preco}")

# # Exercicio 2

MyClient = Cliente.objects.get(id=15)
print(f"{MyClient}, {MyClient.id}")

# # Exercicio 3

Eletronicos = Produto.objects.filter(categoria__nome = 'Eletronicos')
for Elet in Eletronicos:
    print(f"{Elet.nome}")

# # Exercicio 4

Product = Produto.objects.filter(preco__gt = 500).order_by("preco")
for Pro in Product:
    print(f" Produtos : {Pro.nome}, Preco : {Pro.preco}")

# # Exercicio 5

MasterKey = Produto.objects.filter(nome__icontains="S")
for Mas in MasterKey:
    print(f"Produtos com S : {Mas.nome}")

# # Exercicio 6

# Games = Categoria.objects.create(id = 6, nome = "Games")
# print("Created Categoria Games com sucesso!")

# # Exercicio 7

Livros = Produto.objects.filter(categoria__nome__icontains = "Livro").update(estoque = F('estoque') + 10)

print(f"{Livros} livros atualizados")


# # Exercicio 8

Pedidos_com_C = Pedido.objects.filter(status="C").delete()
print(f"{Pedidos_com_C} pedidos excluidos")


# # Exercicio 9


total_estoque = Produto.objects.aggregate(valor_total=Sum(F('preco') * F('estoque')))

print(f"Valor total do estoque: {total_estoque['valor_total']}")


# Exercicio 10

CliCli = Cliente.objects.filter(pedidos__itens__produto_id = 48)
print(f"{CliCli}")
