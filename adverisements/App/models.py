from django.db import models


# Create your models here.
class Adverisements(models.Model):
    # название - title
    # описание -description
    # цена - price
    # торг - auction
    # создано - created
    # изменено - updated
    id = models.CharField("id", max_length=64, primary_key=True)

    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    auction = models.BooleanField(
        default=False,
        verbose_name='Торг'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновлния'
    )

    def __str__(self):
        return f"Adverisements: Adverisements(id={self.id}, title={self.title}, price={self.price})"


class Meta:
    db_table = 'advertisements'
