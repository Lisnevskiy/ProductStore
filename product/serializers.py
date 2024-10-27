from rest_framework import serializers

from .models import Price, Product, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["id", "name", "description"]


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ["id", "currency", "amount"]


class ProductSerializer(serializers.ModelSerializer):
    type = TypeSerializer()
    price = PriceSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "quantity", "barcode", "updated_at", "type", "price"]

    def create(self, validated_data):
        # Извлекаем данные для вложенных объектов
        type_data = validated_data.pop("type")
        price_data = validated_data.pop("price")

        # Пытаемся получить существующий тип по имени, если нет - создаем новый
        type_instance, _ = Type.objects.get_or_create(name=type_data["name"], defaults=type_data)

        # Создаем или получаем связанные объекты
        price_instance = Price.objects.create(**price_data)

        # Создаем продукт с вложенными объектами
        product = Product.objects.create(type=type_instance, price=price_instance, **validated_data)
        return product
