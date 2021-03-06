from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions as p, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Category, Comment
from .serializers import ProductSerializer, \
    CategorySerializer, CreateUpdateProductSerializer, CommentSerializer, ProductListSerializer
from .filters import ProductFilter

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# class ProductsList(APIView): #View
#     def get(self, request):
#         products = P1roduct.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)


# class ProductsList(ListAPIView):
#     queryset         = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductDetail(RetrieveAPIView):
#     queryset         = Product.objects.all()
#     serializer_class = ProductSerializer


# class CreateProduct(CreateAPIView):
#     queryset           = Product.objects.all()
#     permission_classes = [p.IsAdminUser]
#     serializer_class   = CreateUpdateProductSerializer


# class UpdateProduct(UpdateAPIView):
#     queryset           = Product.objects.all()
#     permission_classes = [p.IsAdminUser]
#     serializer_class   = CreateUpdateProductSerializer


# class DeleteProduct(DestroyAPIView):
#     queryset           = Product.objects.all()
#     permission_classes = [p.IsAdminUser]


class MyPaginationClass(PageNumberPagination):
    page_size = 1


class CategoriesList(ListAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset  = Product.objects.all()
    pagination_class = MyPaginationClass
    filter_backends  = [DjangoFilterBackend]
    # filterset_fields = ['categories']
    filter_class = ProductFilter


    def get_serializer_class(self):
        if  self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductSerializer
        return CreateUpdateProductSerializer


    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:
            permissions = []
        else:
            permissions = [p.IsAdminUser]
        return [permission() for permission in permissions]


    @action(methods=['get'], detail=False)
    def search(self, request):
        q  = request.query_params.get('q')
        queryset = self.get_queryset()
        if q is not None:
            queryset = queryset.filter(Q(title__icontains=q) |
                                    Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreate(CreateAPIView):
    queryset  =  Comment.objects.all()
    serializer_class  =  CommentSerializer
    permission_classes = [p.IsAuthenticated]

    def perform_create(sekf, serializer):
        serializer.save(author=self.request.user)

