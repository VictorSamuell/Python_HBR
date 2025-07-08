print("AULA 3")
print("Listas")

lista = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10]
print(lista)

lista2 = ["a", "b", "c", "d", "e" , "f", "g", "h", "i", "j"]
print(lista2)

reversa = lista2[::-1]
print(reversa)

lista.reverse()
print(lista)


lista.append(11)
print(lista)


lista2.append("k")
print(lista2)


#faça um pop remove 
lista.pop()
print(lista)
lista2.pop(0)  
print(lista2)


#


# Django é um framework web em Python para criar sites e APIs rapidamente.
# Tutorial básico do que você precisa saber:

# 1. Instalação:
# pip install django

# 2. Criar um novo projeto:
# django-admin startproject meu_projeto

# 3. Entrar na pasta do projeto:
# cd meu_projeto

# 4. Criar um novo app (aplicação):
# python manage.py startapp meu_app

# 5. Registrar o app em settings.py (INSTALLED_APPS)

# 6. Criar modelos (models.py) para o banco de dados

# 7. Rodar as migrações:
# python manage.py makemigrations
# python manage.py migrate

# 8. Criar um superusuário para acessar o admin:
# python manage.py createsuperuser

# 9. Rodar o servidor:
# python manage.py runserver

# 10. Criar views, urls e templates para exibir páginas

# Documentação oficial: https://docs.djangoproject.com/


# Exemplos de comandos principais do Django mais utilizados no mercado:

# Criar um novo projeto Django
# django-admin startproject nome_do_projeto

# Criar um novo app dentro do projeto
# python manage.py startapp nome_do_app

# Rodar o servidor de desenvolvimento
# python manage.py runserver

# Criar migrações para alterações no banco de dados
# python manage.py makemigrations

# Aplicar as migrações ao banco de dados
# python manage.py migrate

# Criar um superusuário para acessar o admin
# python manage.py createsuperuser

# Criar um novo usuário via shell
# python manage.py shell
# >>> from django.contrib.auth.models import User
# >>> User.objects.create_user('usuario', password='senha')

# Listar todas as rotas do projeto
# python manage.py show_urls  # (pode ser necessário instalar django-extensions)

# Executar testes automatizados
# python manage.py test

# Coletar arquivos estáticos para produção
# python manage.py collectstatic

# Acessar o shell interativo do Django
# python manage.py shell

# Documentação oficial: https://docs.djangoproject.com/