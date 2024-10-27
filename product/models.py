from django.db import models


class Type(models.Model):
    """Представляет категорию типа товара"""

    name = models.CharField(max_length=255, unique=True)
    """Уникальное название типа"""
    description = models.TextField(blank=True, null=True)
    """Необязательное описание типа"""

    def __str__(self):
        """Возвращает строковое представление названия типа"""

        return self.name


class Price(models.Model):
    """Представляет цену товара с указанием валюты и суммы"""

    currency = models.CharField(max_length=3)
    """3-буквенный код валюты, например, RUB"""
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    """Сумма цены, поддерживает до 10 цифр с 2 знаками после запятой"""

    def __str__(self):
        """Возвращает строковое представление цены в формате <сумма + валюта>"""
        return f"{self.amount} {self.currency}"


class Product(models.Model):
    """Представляет продукт с атрибутами, такими как название, количество, штрихкод, и связанные тип и цена"""

    name = models.CharField(max_length=255)
    """Название продукта"""
    quantity = models.PositiveIntegerField()
    """Количество продукта на складе"""
    barcode = models.CharField(max_length=13, unique=True)
    """Уникальный штрихкод продукта, ограниченный 13 символами"""
    updated_at = models.DateTimeField(auto_now=True)
    """Дата и время последнего обновления информации о продукте"""

    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="products")
    """Связь с категорией типа товара. При удалении типа все связанные продукты также будут удалены"""
    price = models.OneToOneField(Price, on_delete=models.CASCADE, related_name="product")
    """Связь с объектом цены продукта. При удалении продукта цена также удаляется"""

    def __str__(self):
        """Возвращает строковое представление названия продукта"""

        return self.name
