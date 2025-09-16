# loja/management/commands/populate_db.py
import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from faker import Faker
from Store.models import Cliente, Categoria, Produto, Pedido, ItemPedido

class Command(BaseCommand):
    help = 'Popula o banco de dados com 50 registros em cada tabela'

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando o povoamento do banco de dados...")

        fake = Faker('pt_BR')

        # Limpando dados existentes para evitar duplicatas
        self.stdout.write("Limpando tabelas antigas...")
        ItemPedido.objects.all().delete()
        Pedido.objects.all().delete()
        Produto.objects.all().delete()
        Categoria.objects.all().delete()
        Cliente.objects.all().delete()

        # --- Gerar 50 Clientes ---
        clientes = []
        for _ in range(50):
            clientes.append(Cliente(nome=fake.name(), email=fake.unique.email()))
        Cliente.objects.bulk_create(clientes)
        self.stdout.write(self.style.SUCCESS('50 Clientes criados com sucesso!'))

        # --- Gerar 5 Categorias (para ter variedade nos produtos) ---
        nomes_categorias = ['Eletrônicos', 'Livros', 'Roupas', 'Casa e Cozinha', 'Esportes']
        categorias = []
        for nome in nomes_categorias:
            categorias.append(Categoria(nome=nome))
        Categoria.objects.bulk_create(categorias)
        self.stdout.write(self.style.SUCCESS(f'{len(nomes_categorias)} Categorias criadas com sucesso!'))

        # --- Gerar 50 Produtos ---
        # Certificar que as categorias foram salvas e obter os objetos
        lista_categorias = list(Categoria.objects.all())
        produtos = []
        for _ in range(50):
            produtos.append(Produto(
                nome=fake.word().capitalize() + ' ' + fake.word().capitalize(),
                descricao=fake.text(max_nb_chars=200),
                preco=Decimal(random.uniform(10.50, 999.99)),
                categoria=random.choice(lista_categorias),
                estoque=random.randint(10, 100)
            ))
        Produto.objects.bulk_create(produtos)
        self.stdout.write(self.style.SUCCESS('50 Produtos criados com sucesso!'))

        # --- Gerar 50 Pedidos ---
        lista_clientes = list(Cliente.objects.all())
        pedidos = []
        for _ in range(50):
            pedidos.append(Pedido(
                cliente=random.choice(lista_clientes),
                status=random.choice(['P', 'A', 'C'])
            ))
        Pedido.objects.bulk_create(pedidos)
        self.stdout.write(self.style.SUCCESS('50 Pedidos criados com sucesso!'))

        # --- Gerar 50 Itens de Pedido ---
        lista_pedidos = list(Pedido.objects.all())
        lista_produtos = list(Produto.objects.all())
        itens_pedido = []
        for i in range(50):
            produto_escolhido = random.choice(lista_produtos)
            itens_pedido.append(ItemPedido(
                # Reutilizando os pedidos já criados para garantir 1 item por pedido no mínimo
                pedido=lista_pedidos[i],
                produto=produto_escolhido,
                quantidade=random.randint(1, 5),
                preco_unitario=produto_escolhido.preco
            ))
        ItemPedido.objects.bulk_create(itens_pedido)
        self.stdout.write(self.style.SUCCESS('50 Itens de Pedido criados com sucesso!'))

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
