from django.contrib import admin
from .models import User, Product, Order


@admin.action(description="Обнулить количество")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class UserAdmin(admin.ModelAdmin):
    """Список Клиентов"""
    list_display = ['id', 'name', 'email', 'phone_number', 'address', 'date_added']
    list_filter = ['name', 'phone_number', 'address']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя Клиента (name)'
    actions = [reset_quantity]

    """Отдельный Клиент"""
    readonly_fields = ['date_added']
    fieldsets = [
        (
            'Имя Клиента',
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контакты',
            {
                'classes': ['wide'],
                'description': 'Email, номер телефона и адрес Клиента',
                'fields': ['email', 'phone_number', 'address'],
            },
        ),
        (
            'Дата регистрации',
            {
                'classes': ['collapse'],
                'description': 'Заполняется автоматически',
                'fields': ['date_added'],
            },
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['id', 'name', 'quantity', 'date_added', 'price']
    list_filter = ['name', 'quantity', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный Продукт"""
    readonly_fields = ['date_added']
    fieldsets = [
        (
            'Название и описание продукта',
            {
                'classes': ['wide'],
                'fields': ['name', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'classes': ['wide'],
                'description': 'Количество и цена',
                'fields': ['quantity', 'price'],
            },
        ),
        (
            'Дата добавления',
            {
                'classes': ['collapse'],
                'description': 'Заполняется автоматически',
                'fields': ['date_added'],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    """Список заказов"""
    list_display = ['id', 'customer', 'date_added', 'total_price_products']
    list_filter = ['customer']
    actions = [reset_quantity]

    """Отдельный Заказ"""
    readonly_fields = ['date_added']
    fieldsets = [
        (
            'Клиент',
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Продукты',
            {
                'classes': ['wide'],
                'fields': ['products'],
            },
        ),
        (
            'Дата заказа',
            {
                'classes': ['collapse'],
                'description': 'Заполняется автоматически',
                'fields': ['date_added'],
            },
        ),
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
