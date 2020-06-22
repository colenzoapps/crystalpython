from rest_framework import serializers
from frontend.models import (Branch, User, Order, Department, Product, Customer, Status, Priority)
# from djoser.serializers import UserCreateSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
	    model = User
	    fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'password', 'password2']
	    extra_kwargs = {'password': {'write_only': True},}	

    def	save(self):
        account = User(
                        email=self.validated_data['email'],
                        username=self.validated_data['email'],
                        staff_Id='12345'
                    )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class MobileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username','password','first_name','last_name','phone')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class JsonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','first_name','last_name','is_active','phone','location','image')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(required=False, allow_null=True,format=None, input_formats=None)
    due_date = serializers.DateTimeField(required=False, allow_null=True,format=None, input_formats=None)
    createdOn = serializers.DateTimeField(required=False, allow_null=True,format=None, input_formats=None)
    lastEditOn = serializers.DateTimeField(required=False, allow_null=True,format=None, input_formats=None)

    class Meta:
        model = Order
        fields = '__all__'



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'


# class RegisterSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id','email','username','password','first_name','last_name')