from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions

from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet
                   ):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = OrderSerializer(data=data, context={'requset': request})
    #     if serializer.is_valid(raise_exception=True):
    #         order = serializer.save()

