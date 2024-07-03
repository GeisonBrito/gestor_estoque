
from django.shortcuts import redirect, render

from .forms import LocalForm, EmbalagemForm
from .models import Local, Embalagem


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

def listar_embalagens(request):
    consulta = request.GET.get('q')
    sigla = request.GET.get('sigla')
    embalagens = Embalagem.objects.all()
    if consulta:
        embalagens = embalagens.filter(nome__icontains=consulta)
    if sigla:
        embalagens = embalagens.filter(sigla=sigla)
    return render(request, 'produtos/listar_embalagens.html', {'embalagens': embalagens})

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
    embalagem = Embalagem.objects.filter(id=id).first()
    if request.method == 'POST':
        form = EmbalagemForm(request.POST, instance=embalagem)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm(instance=embalagem)
    return render(request, 'produtos/adicionar_embalagem.html', {'form': form}) 

def excluir_embalagem(request, id):
    embalagem = Embalagem.objects.filter(id=id).first()
    if request.method == 'GET':
        embalagem.delete()
        return redirect('listar_embalagens')