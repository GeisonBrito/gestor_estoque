from django.db import models


class BaseModel(models.Model):
    criado_em = models.DateField(
        auto_now_add=True,
    )
    atualizado_em = models.DateField(
        auto_now=True,
    )

    class Meta:
        abstract = (True,)
