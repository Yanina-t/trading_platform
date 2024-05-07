from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Suppliers, Product


class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier_link', 'level', 'debt_to_supplier', 'city', 'created_at')  # Отображение в списке объектов
    list_filter = ('city',)  # Фильтр по полю города
    actions = ['clear_debt']  # Действие для очистки задолженности

    def supplier_link(self, obj):
        if obj.supplier:
            url = f"/admin/network/suppliers/{obj.supplier.id}/change/"  # URL к админке поставщика
            return format_html(f'<a href="{url}">{obj.supplier.name}</a>')
        return "-"
    supplier_link.short_description = 'Поставщик'  # Название колонки

    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)  # Обновление задолженности для выбранных объектов
    clear_debt.short_description = "Очистить задолженность "  # Название действия

    def save_model(self, request, obj, form, change):
        try:
            obj.save()  # Попытка сохранить объект
        except ValueError as e:
            # Обработка исключения ValueError
            messages.error(request, f"Ошибка при сохранении: {e}")  # Выводим сообщение об ошибке
            return


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'release_date')  # Отображение в списке объектов


admin.site.register(Product, ProductAdmin)
admin.site.register(Suppliers, SuppliersAdmin)
