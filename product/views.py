from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Price, Product, Type
from .serializers import PriceSerializer, ProductSerializer, TypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"])
    def reduce_stock(self, request, pk=None):
        product = self.get_object()
        amount = request.data.get("amount", 1)

        # Валидация значения amount
        if not isinstance(amount, int) or amount <= 0:
            return Response(
                {"error": "Invalid amount. Please provide a positive integer."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Проверка, достаточно ли остатков
        if product.quantity >= amount:
            product.quantity -= amount
            product.save()
            return Response(
                {
                    "status": "Stock reduced",
                    "product_id": product.id,
                    "remaining_stock": product.quantity
                },
                status=status.HTTP_200_OK
            )

        # Недостаточно остатков
        return Response(
            {
                "error": "Not enough stock",
                "requested_amount": amount,
                "available_stock": product.quantity
            },
            status=status.HTTP_400_BAD_REQUEST
        )


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
