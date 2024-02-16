from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get a list of items",
        responses={200: ItemSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                name="category",
                in_=openapi.IN_QUERY,
                description="Filter items by category",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                name="stock_status",
                in_=openapi.IN_QUERY,
                description="Filter items by stock status",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Parse query parameters
        category = request.GET.get('category')
        stock_status = request.GET.get('stock_status')

        # Filter queryset based on query parameters
        if category:
            queryset = queryset.filter(category__name=category)

        if stock_status:
            queryset = queryset.filter(stock_status=stock_status)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
