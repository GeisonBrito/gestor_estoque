from django.shortcuts import redirect, render

from .forms import CategoriaForm, EmbalagemForm, LocalForm
from .models import Categoria, Embalagem, Local


def inicio(request):
    return render(request, 'menu.html')


def listar_locais(request):
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()
    if consulta:
        locais = locais.filter(nome__icontains=consulta)
    if tipo:
        locais = locais.filter(tipo=tipo)
    return render(request, 'produtos/listar_locais.html', {'locais': locais})


def adicionar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm()
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def editar_local(request, id):
    local = Local.objects.filter(id=id).first()
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def excluir_local(request, id):
    local = Local.objects.filter(id=id).first()
    if request.method == 'GET':
        local.delete()
        return redirect('listar_locais')


def listar_embalagens(request):
    consulta = request.GET.get('q')
    sigla = request.GET.get('sigla')
    embalagens = Embalagem.objects.all()
    if consulta:
        embalagens = embalagens.filter(nome__icontains=consulta)
    if sigla:
        embalagens = embalagens.filter(sigla=sigla)
    return render(request, 'produtos/listar_embalagens.html', {'embalagens': embalagens})  # noqa: E501


def adicionar_embalagem(request):
    if request.method == 'POST':
        form = EmbalagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm()
    return render(request, 'produtos/adicionar_embalagem.html', {'form': form})


def editar_embalagem(request, id):
    embalagem = Embalagem.objects.get(id=id)
    if request.method == 'POST':
        form = EmbalagemForm(request.POST, instance=embalagem)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm(instance=embalagem)
    return render(request, 'produtos/adicionar_embalagem.html', {'form': form})


def excluir_embalagem(request, id):
    embalagem = Embalagem.objects.get(id=id)
    embalagem.delete()
    return redirect('listar_embalagens')


def listar_categorias(request):
    nome = request.GET.get('nome')
    categorias = Categoria.objects.all()
    if nome:
        categorias = categorias.filter(nome__icontains=nome)
    return render(
        request, 'produtos/listar_categorias.html', {'categorias': categorias}
    )


def adicionar_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'produtos/adicionar_categoria.html', {'form': form})


def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'produtos/editar_categorias.html', {'form': form})


def excluir_categoria(request, id):
    categoria = Categoria.objects.filter(id=id)
    categoria.delete()
    return redirect('listar_categorias')
