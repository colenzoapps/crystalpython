from django.shortcuts import render, redirect
from .forms import UserChangeForm, UserForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.db import transaction
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from frontend.models import *
from crystalp.serializers import *
from rest_framework import status, viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.cache import cache_page
from rest_framework import mixins, generics


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        # profile_form = ProfileForm(request.POST, instance=request.user.profile)
        update_user = user_form.save(commit=False)
        if user_form.is_valid():
            if request.FILES:
                update_user.image = request.FILES['image']
                update_user.save()
            else:
                update_user.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('frontend:update_profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
    })


# @login_required
# def clients(request):
#     return render(request, 'clients.html')


# @login_required
# def appointments(request):
#     return render(request, 'appointments.html')


# @login_required
# def device_page(request):
#     return render(request, 'device.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


#---------API LIST -------------
# @api_view(['GET', 'POST'])
# def device_list(request):
#     if request.method == 'GET':
#         snippets = Devices.objects.all()
#         serializer = DeviceSerializer(snippets, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = DeviceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def device_details(request, pk):
#     try:
#         device = Devices.objects.get(pk=pk)
#     except Devices.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DeviceSerializer(device)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = DeviceSerializer(device, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         device.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class ClientList(generics.ListCreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientsSerializer
    
#     # def get_queryset(self):
#     #     queryset = Client.objects.all()
#     #     depot = self.request.query_params.get('depot', None)
#     #     if depot is not None:
#     #         queryset = queryset.filter(depot=depot)
#     #     return queryset

#     def list(self, request, **kwargs):
#         queryset = self.get_queryset()
#         serializer = ClientsSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientsSerializer

#     # def retrieve(self, request, *args, **kwargs):
#     #     pk = self.kwargs.get('pk')
#     #     plan = queryset.get(pk=kwargs['pk'])
#     #     serializer = ClientsSerializer(plan)
#     #     return Response(serializer.data)

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class CarePlanList(APIView):
#     def get(self, request, format=None):
#         queryset = CarePlan.objects.all()
#         serializer = CarePlanSerializer(queryset, many=True)
#         return Response(serializer.data)


# class CareProviderList(APIView):
#     def get(self, request, format=None):
#         queryset = CareProvider.objects.all()
#         serializer = CareProviderSerializer(queryset, many=True)
#         return Response(serializer.data)


# class BranchList(APIView):
#     def get(self, request, format=None):
#         queryset = Branch.objects.all()
#         serializer = BranchSerializer(queryset, many=True)
#         return Response(serializer.data)


# class StatusList(APIView):
#     def get(self, request, format=None):
#         queryset = Status.objects.all()
#         serializer = StatusSerializer(queryset, many=True)
#         return Response(serializer.data)