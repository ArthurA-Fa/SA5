from django.shortcuts import render, redirect
from .models import Pessoa
dados = []

# Create your views here.
def home(request):
    nome = ""
    email = ""
    ani = 0
    pais = ""

    dados = Pessoa.objects.all()

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        ani = request.POST.get("ani",0)
        pais = request.POST.get("pais")
        Pessoa.objects.create(nome=nome, email=email, ani=ani, pais=pais )

    return render(request, "site_app/global/home.html", context={"dados":dados,"nome":nome,"email":email,"ani":ani,"pais":pais})

def deletar(request,id=0):
    pessoa = {}
    if id:
        pessoa = Pessoa.objects.get(id=id)
        pessoa.delete()
        return redirect(deletar)
    
    nome_Filter = request.POST.get("nome")
    if nome_Filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome_icontains = nome_Filter)
    else:
        pessoa["pessoas"] = Pessoa.objects.all()
    return render(request, "site_app/global/deletar.html", context=pessoa)

def atualizar(request,id=0):
    pessoa = {}
    if id:
        if request.POST:
            pessoa = Pessoa.objects.get(id=id) 
            pessoa.nome = request.POST.get("nome", pessoa.nome)
            pessoa.email = request.POST.get("email", pessoa.email)
            pessoa.ani = request.POST.get("ani", pessoa.ani)
            pessoa.pais = request.POST.get("pais", pessoa.pais)

            pessoa.save()
            return redirect(atualizar)
        

        pessoa["pessoa"] = Pessoa.objects.all(id=id)
        return render(request, "site_app/partials/update.html", pessoa)
    
    nome_Filter = request.POST.get("nome")
    if nome_Filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome_icontains = nome_Filter)
    else:
        pessoa["pessoas"] = Pessoa.objects.all()
    return render(request, "site_app/global/atualizar.html", context=pessoa)

def pesquisar(request):
    pessoa = {}
    nome_Filter = request.POST.get("nome")
    if nome_Filter:
        pessoa["pessoas"] = Pessoa.objects.filter(nome_icontains = nome_Filter)
    else:
        pessoa["pessoas"] = Pessoa.objects.all()

    return render(request, "site_app/global/pesquisar.html", pessoa)

def criar(request):
    nome = ""
    email = ""
    ani = 0
    pais = ""

    dados = Pessoa.objects.all()

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        ani = request.POST.get("ani",0)
        pais = request.POST.get("pais")
        Pessoa.objects.create(nome=nome, email=email, ani=ani, pais=pais )

    return render(request, "site_app/global/criar.html", context={"dados":dados,"nome":nome,"email":email,"ani":ani,"pais":pais})
