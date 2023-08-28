from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

User = get_user_model()


def get_user_model():
    pass


# Create your models here.
class Adverisements(models.Model):
    # название - title
    # описание -description
    # цена - price
    # торг - auction
    # создано - created
    # изменено - updated
    # id = models.CharField("id", max_length=64, primary_key=True)

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
    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE
    )
    image = models.ImageField('Изображения', upload_to='adverisements/')

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color:green">Сегодня в {} </span>', created_time)
        return self.created_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color:yellow"> Сегодня в {} </span>', updated_time)
        return self.updated_at.strftime("%d.%m.%y в %H:%M:%S")

    @admin.display(description='фото')
    def get_html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )

    def __str__(self):
        return f"Adverisements(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = 'advertisements'
