from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django import forms
from crispy_forms.layout import Field, Layout, Submit, Row, Column, Div, ButtonHolder
from crispy_forms.helper import FormHelper
from .widgets import BootstrapDateTimePickerInput



class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2', )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        FormHelper.use_custom_control = True

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()

        return user



class CustomDatePicker(Field):
    template = 'custom_datepicker.html'



class UserForm(forms.ModelForm):
    # dob = forms.DateField(input_formats=['%Y/%m/%d'], widget=BootstrapDateTimePickerInput())
    class Meta:
        model = User
        fields = ('email','phone','location','image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = False
        self.fields['image'].required = False
        self.fields['location'].required = False
        self.helper = FormHelper(self)
        FormHelper.use_custom_control = True
        self.helper = FormHelper()

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        # user.gender = self.cleaned_data['gender']
        # user.phone = self.cleaned_data['phone']
        # user.location = self.cleaned_data['location']
        # user.image = self.cleaned_data['image']

        if commit:
            user.save()

        return user


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('organisation','name','code','address','city','postcode')