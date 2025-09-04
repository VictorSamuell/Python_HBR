from django.shortcuts import render
from blog.models import Post

def posts_web(request):
    posts = Post.objects.filter(autor__nome='Ana Coder', conteudo__icontains='web')

    return render(request, 'posts_web.html', {'posts': posts})