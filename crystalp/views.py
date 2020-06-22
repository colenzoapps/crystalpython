from django.shortcuts import render, redirect, reverse
from rest_framework import viewsets, permissions, status
from frontend.models import *
from .serializers import *
from frontend.forms import RegistrationForm
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import status, pagination
from django.http import Http404, JsonResponse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.decorators import permission_required, login_required
from rest_framework.decorators import api_view, permission_classes, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.cache import cache_page
from rest_framework import mixins, generics
import json
from datetime import datetime
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication


@login_required
def home(request):
    return render(request, 'home.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = JsonUserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user.username)


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        context['form'] = RegistrationForm()

    return render(request, 'register.html', context)

# API LIST 

class StatusList(APIView):
    def get(self, request, format=None):
        queryset = Status.objects.all()
        serializer = StatusSerializer(queryset, many=True)
        return Response(serializer.data)


class PriorityList(APIView):
    def get(self, request, format=None):
        queryset = Priority.objects.all()
        serializer = StatusSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    # def get_queryset(self):
    #     queryset = Order.objects.all()
    #     depot = self.request.query_params.get('depot', None)
    #     if depot is not None:
    #         queryset = queryset.filter(depot=depot)
    #     return queryset

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     plan = queryset.get(pk=kwargs['pk'])
    #     serializer = OrderSerializer(plan)
    #     return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)