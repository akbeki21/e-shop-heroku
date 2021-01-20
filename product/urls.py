from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoriesList, ProductViewSet


router = DefaultRouter()
router.register('', ProductViewSet)

# products = ProductViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
#     'patch': 'partial_update',
#     'post': 'create',
#     'delete': 'destroy',
# })

urlpatterns = [
    path('categories/', CategoriesList.as_view()),
    path('', include(router.urls)),
    
    # path('', products),
    # path('<str:pk>/', products),
    # path('', ProductsList.as_view()),
    # path('detail/<str:pk>/', ProductDetail.as_view()),
    # path('create/', CreateProduct.as_view()),
    # path('update/<str:pk>/', UpdateProduct.as_view()),
    # path('delete/<str:pk>/', DeleteProduct.as_view()),


]