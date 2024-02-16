from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import ItemList, APIRoot
from rest_framework.renderers import OpenAPIRenderer

# Define your router
router = DefaultRouter()
router.register(r'items', ItemList, basename='item')

# Define your API schema view
schema_view = get_schema_view(
    title='API',
    url='http://127.0.0.1:8000/',
    renderer_classes=[OpenAPIRenderer]
)

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('items/', ItemList.as_view(actions={'get': 'list', 'post': 'create'}), name='item-list'),
    path('api/docs/', schema_view, name='api-docs'),
]