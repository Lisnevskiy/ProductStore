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

        if product.quantity >= amount:
            product.quantity -= amount
            product.save()
            return Response({"status": "stock reduced"}, status=status.HTTP_200_OK)
        return Response({"error": "Not enough stock"}, status=status.HTTP_400_BAD_REQUEST)


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
