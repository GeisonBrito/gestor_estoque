from os import name
from django.db import models

from utils.base_models import BaseModel


class Embalagem(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name="Nome da embalagem",
    )
    sigla = models.CharField(
        max_length=3,
        verbose_name="Sigla da embalagem",
    )

    class Meta:
        db_table = "embalagem"

    def __str__(self):
        return self.name


class Local(BaseModel):
    TIPOS_DE_LOCAL = [("F", "Físico"), ("D", "Digital")]
    nome = models.CharField(
        max_length=50, verbose_name="Nome do local armazenado", unique=True
    )
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS_DE_LOCAL,
        verbose_name="Tipo do local movimentado",
    )

    class Meta:
        db_table = "locais"


class Movimentacao(BaseModel):
    TIPOS_MOVIMENTACAO = [
        (1, "Entrada"),
        (-1, "Saída"),
    ]
    produto = models.ForeignKey(
        "produtos.Produto",
        on_delete=models.CASCADE,
        verbose_name="Produto da movimentação",
    )
    fornecedor = models.ForeignKey(
        "produtos.Fornecedor",
        on_delete=models.CASCADE,
        verbose_name="Fornecedor do produto movimentado",
    )
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=6, verbose_name="Quantidade movimentada"
    )
    local = models.ForeignKey(
        "produtos.Local",
        on_delete=models.CASCADE,
        verbose_name="Local da movimentação",
    )
    tipo = models.IntegerField(
        choices=TIPOS_MOVIMENTACAO,
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        verbose_name="Preço do produto na movimentacao"
    )
    codigo_fabricante = models.CharField(
        max_length=20,
        verbose_name="Código do fabricante"
    )
    class Meta:
        db_table = "movimentacao"

    def __str__(self):
        return self.name


class Fornecedor(BaseModel):
    nome_social = models.CharField(
        max_length=100, verbose_name="Razao Social do Fornecedor"
    )
    nome_fantasia = models.CharField(
        max_length=100, verbose_name="Nome Fantasia do Fornecedor"
    )
    produtos = models.ManyToManyField(
        "produtos.Produto",
        verbose_name="Produtos do Fornecedor",
    )

    class Meta:
        db_table = "fornecedor"

    def __str__(self):
        return self.name


class Produto(BaseModel):
    nome = models.CharField(
        max_length=100,
        verbose_name='nome do produto',
    )
    categoria = models.ForeignKey(
        'produtos.Categoria',
        on_delete=models.CASCADE,
        verbose_name='categoria do produto',
    )
    embalagens = models.ManyToManyField(
        'produtos.Embalagem',
        verbose_name='Embalagens do produto',
    )
    estoque_minimo = models.FloatField(
        verbose_name='Estoque minimo do produto',
    )
    estoque_maximo = models.FloatField(
        verbose_name='Estoque maximo do produto',
    )

    class Meta:
        db_table = 'produtos'

    def get_nome_completo(self):
        return f"{self.nome} ({', '.join([e.nome for e in self.embalagens.all()])})"  # noqa: E501

    def __str__(self):
        return self.get_nome_completo()


class Categoria(BaseModel):
    name = models.CharField(
        max_length=100, verbose_name='nome da categoria', unique=True
    )

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.name
