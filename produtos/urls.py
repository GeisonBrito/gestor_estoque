
from django.urls import path

from .views import (
    adicionar_categorias,
    adicionar_embalagem,
    adicionar_fornecedores,
    adicionar_local,
    adicionar_produtos,
    editar_categoria,
    editar_embalagem,
    editar_fornecedores,
    editar_local,
    editar_produto,
    excluir_categoria,
    excluir_embalagem,
    excluir_fornecedores,
    excluir_local,
    excluir_produto,
    inicio,
    listar_categorias,
    listar_embalagens,
    listar_fornecedores,
    listar_locais,
    listar_produtos,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagens/', listar_embalagens, name='listar_embalagens'),
    path('embalagens/adicionar/', adicionar_embalagem, name='adicionar_embalagens'),  # noqa: E501
    path('embalagem/<int:id>/editar', editar_embalagem, name='editar_embalagem'),  # noqa: E501
    path('embalagem/<int:id>/excluir', excluir_embalagem, name='excluir_embalagem'),  # noqa: E501
    path('local/<int:id>/editar', editar_local, name='editar_local'),
    path('local/<int:id>/excluir', excluir_local, name='excluir_local'),

    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', adicionar_categorias, name='adicionar_categoria'),  # noqa: E501
    path('categoria/editar/<int:id>', editar_categoria, name='editar_categoria'),  # noqa: E501
    path('categoria/excluir/<int:id>', excluir_categoria, name='excluir_categoria'),  # noqa: E501

    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', adicionar_produtos, name='adicionar_produtos'),
    path('produtos/<int:id>/editar', editar_produto, name='editar_produto'),
    path('produtos/<int:id>/excluir', excluir_produto, name='excluir_produto'),

    path('fornecedores/', listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/adicionar/', adicionar_fornecedores, name='adicionar_fornecedores'),  # noqa: E501
    path('editar_fornecedores/<pk>/', editar_fornecedores, name='editar_fornecedores'),  # noqa: E501
    path('excluir_fornecedores/<pk>/', excluir_fornecedores, name='excluir_fornecedores')  # noqa: E501
]
