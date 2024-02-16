from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .models import Item
from .serializers import ItemSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ItemList(ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_extra_actions(self):
        return {
            'list': self.list,
            'create': self.create,
            'retrieve': self.retrieve,
            'update': self.update,
            'partial_update': self.partial_update,
            'destroy': self.destroy,
        }


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
    def get(self, request):
        category = request.GET.get('category')
        stock_status = request.GET.get('stock_status')

        items = Item.objects.all()

        if category:
            items = items.filter(category__name=category)

        if stock_status:
            items = items.filter(stock_status=stock_status)

        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'items': reverse('item-list', request=request, format=format)
        })