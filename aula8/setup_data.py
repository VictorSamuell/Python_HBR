# setup_data.py
from novos.models import Autor, Post, Tag
from django.utils import timezone
import datetime

# Limpando dados antigos
print("Limpando dados antigos...")
Post.objects.all().delete()
Autor.objects.all().delete()
Tag.objects.all().delete()

# Criando Tags
print("Criando Tags...")
tag_python = Tag.objects.create(nome='Python')
tag_django = Tag.objects.create(nome='Django')
tag_sql = Tag.objects.create(nome='SQL')
tag_performance = Tag.objects.create(nome='Performance')

# Criando Autores
print("Criando Autores...")
autor1 = Autor.objects.create(nome='Ana Coder', email='ana.coder@exemplo.com')
autor2 = Autor.objects.create(nome='Bruno Dev', email='bruno.dev@exemplo.com')

# Criando Posts
print("Criando Posts...")
# Post de 2024 com tags
post1 = Post.objects.create(
    titulo='Otimizando com prefetch_related',
    conteudo='Uma olhada profunda em otimização de queries N-N.',
    data_publicacao=timezone.make_aware(datetime.datetime(2024, 5, 20)),
    visualizacoes=1500,
    autor=autor1
)
post1.tags.add(tag_django, tag_performance, tag_sql)

# Post de 2025 com "Django" no título
post2 = Post.objects.create(
    titulo='Novidades do Django 5.0',
    conteudo='Explorando as novas features da versão 5.0.',
    data_publicacao=timezone.make_aware(datetime.datetime(2025, 1, 15)),
    visualizacoes=2200,
    autor=autor1
)
post2.tags.add(tag_django)

# Post de 2025 sem "Django" no título
post3 = Post.objects.create(
    titulo='Programação Assíncrona com Python',
    conteudo='Asyncio e suas vantagens.',
    data_publicacao=timezone.make_aware(datetime.datetime(2025, 3, 10)),
    visualizacoes=850,
    autor=autor2
)
post3.tags.add(tag_python, tag_performance)

# Post de 2024 com apenas uma tag
post4 = Post.objects.create(
    titulo='Consultas SQL Complexas',
    conteudo='Como usar subqueries e CTEs.',
    data_publicacao=timezone.make_aware(datetime.datetime(2024, 11, 30)),
    visualizacoes=1100,
    autor=autor2
)
post4.tags.add(tag_sql)

print("\nBanco de dados populado com sucesso!")
