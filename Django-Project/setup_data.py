from blog.models import Pessoa

print("FUNCIONANDO!")

Pessoa.objects.all().delete()

pessoa1 = Pessoa.objects.create(nome = "Victor Samuel", cpf = "12345678912")
pessoa2 = Pessoa.objects.create(nome = "Danilão", cpf = "87698787654")
