# queries.py
from django.db.models import Q, Count, Avg, Max
from novos.models import Post, Autor

# ===================================================================
# Tópico 1: Otimizando com prefetch_related (Slides 4-6)
# ===================================================================
print("\n--- [Tópico 1: prefetch_related] ---")

# MODO INEFICIENTE: Causa o problema N+1
# Uma query para os posts, e depois UMA NOVA query para as tags de CADA post.
# Total de queries = 1 (posts) + N (tags para cada post) = N+1
print("\nModo Ineficiente (N+1 queries):")
posts_ineficientes = Post.objects.all() # Query 1
for post in posts_ineficientes:
    print(f"\n> Post: {post.titulo}")
    # A linha abaixo dispara uma nova query para CADA post no loop
    tags_do_post = post.tags.all()
    print(f"  Tags: {[tag.nome for tag in tags_do_post]}")

# MODO EFICIENTE: Resolve o problema N+1 com apenas 2 queries
# Query 1: Busca todos os posts.
# Query 2: Busca TODAS as tags de TODOS os posts da primeira consulta de uma só vez.
print("\n\nModo Eficiente (2 queries com prefetch_related):")
posts_eficientes = Post.objects.prefetch_related('tags').all() # Adiciona o prefetch_related
for post in posts_eficientes:
    print(f"\n> Post: {post.titulo}")
    # NENHUMA nova query é feita aqui, as tags já foram pré-buscadas.
    tags_do_post = post.tags.all()
    print(f"  Tags: {[tag.nome for tag in tags_do_post]}")

# ===================================================================
# Tópico 2: Q Objects para Consultas Complexas (Slides 7-10)
# ===================================================================
print("\n\n--- [Tópico 2: Q Objects] ---")

# Objetivo: Encontrar posts publicados em 2024 OU cujo título contém "Django".
# O .filter() por padrão usa AND. Para usar OR, precisamos de Q objects.

# Criando os Q objects que encapsulam cada condição.
condicao_ano = Q(data_publicacao__year=2024)
condicao_titulo = Q(titulo__icontains='Django')

# Combinando as condições com o operador | (OR) e aplicando o filtro.
posts_filtrados = Post.objects.filter(condicao_ano | condicao_titulo)

print("\nPosts de 2024 OU com 'Django' no título:")
for post in posts_filtrados:
    print(f" - '{post.titulo}' (Ano: {post.data_publicacao.year})")

# ===================================================================
# Tópico 3: Funções de Agregação (Slides 11-13)
# ===================================================================
print("\n\n--- [Tópico 3: Funções de Agregação] ---")

# O método .aggregate() calcula valores sobre o QuerySet inteiro e retorna um dicionário.

# 1. Contar o número total de autores.
total_autores = Autor.objects.aggregate(total=Count('id'))
print(f"\nTotal de autores: {total_autores}") # Exemplo de saída: {'total': 2}

# 2. Encontrar a data de publicação do post mais recente.
post_mais_recente = Post.objects.aggregate(mais_recente=Max('data_publicacao'))
print(f"Post mais recente: {post_mais_recente}")

# 3. Calcular a média de visualizações de todos os posts.
media_visualizacoes = Post.objects.aggregate(media_views=Avg('visualizacoes'))
print(f"Média de visualizações: {media_visualizacoes}")

# 4. Contar quantos posts a Ana (autor id=1, no nosso setup) escreveu.
posts_da_ana = Post.objects.filter(autor__nome='Ana Coder').aggregate(total=Count('id'))
print(f"Total de posts da Ana Coder: {posts_da_ana}")

