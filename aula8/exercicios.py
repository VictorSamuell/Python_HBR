from novos.models import Autor, Post, Tag
from django.db.models import Value
from django.db.models.functions import Conca
print("\n===============")
print("DJANGO")
print("===============")

post = Post.objects.filter(titulo__icontains="Python")
print(f"{post}")

posts_2023 = Post.objects.filter(data_publicacao__year=2023)
print(posts_2023)

for posts in posts_2023:
    print(f"{posts.id}")


autor = Autor.objects.filter(nome__icontains="Ana")
print(f"{autor}")


AnaCo = Autor.objects.get(id=1)
print(f"Ana Coder :: {AnaCo.nome}")

pos = Post.objects.filter(visualizacoes__lt=500 ,data_publicacao__year=2023)
n = 1
for p in pos:
    print(f"Post {n}: {p}")
    n += 1











# # Exercício 1
# posts_ana_web = Post.objects.filter(
#     autor__nome="Ana Coder",
#     conteudo__icontains="web"
# )
# for p in posts_ana_web:
#     print(f" {p.titulo}")
# # Exercício 2
# tag_otimizacao, created = Tag.objects.get_or_create(nome="Otimização")
# post_otimizacao = Post.objects.get(titulo="Otimizando Queries no Django")
# post_otimizacao.tags.add(tag_otimizacao)
# print(f"Tags do post '{post_otimizacao.titulo}': {[t.nome for t in post_otimizacao.tags.all()]}")
# # Exercício 3
# posts_sem_python = Post.objects.exclude(tags__nome="Python")
# for p in posts_sem_python:
#     print(f"Apagando: {p.titulo}")
#     p.delete()
# # Exercício 4
# num = Post.objects.filter(data_publicacao__year__lt=2025).update(
#     titulo=Concat(Value("[ANTIGO] "), "titulo")
# )
# print(f"{num} posts atualizados")
# # Exercício 
# for post in Post.objects.select_related("autor").all():
#     print(f" - '{post.titulo}' por {post.autor.nome}")
