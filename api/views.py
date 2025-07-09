from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Order, OrderSen
from .serializers import OrderSerializer, UserSerializer, OrderSenSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# User Views
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

@csrf_exempt
def delete_user(request, pk):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
    return JsonResponse({'message': 'Invalid request'}, status=400)

# Order Views
class OrderListCreate(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

# OrderSen Views
class OrderSenListCreate(generics.ListCreateAPIView):
    serializer_class = OrderSenSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrderSen.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class OrderSenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderSen.objects.all()
    serializer_class = OrderSenSerializer
    permission_classes = [IsAuthenticated]

