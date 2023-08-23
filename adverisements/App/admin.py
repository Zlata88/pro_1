from django.contrib import admin
from .models import Adverisements


# Register your models here.
class AdverisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction']
    list_filter = ('title', 'price', 'created_at')
    actions = ['make_auctions_as_false', 'make_auctions_as_true']  # добавили новое действие в меню
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction')
        })
    )  # красиво размещаем смысловые блоки

    @admin.action(
        description='Убрать возможность торга')  # добавили функцию декоратор, которая добавляет к функции описание
    def make_auctions_as_true(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(
        description='Добавить возможность торга')  # добавили функцию декоратор, которая добавляет к функции описание
    def make_auctions_as_false(self, request, queryset):
        queryset.update(auction=True)

    pass


admin.site.register(Adverisements, AdverisementsAdmin)
