from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users
from ...apps.utils.forms_date import DateInput

class UsersModelForm(UserCreationForm):

    class Meta:
        model = Users
        exclude = ('created_at', 'updated_at', 'groups', 'user_permissions',
            'last_login', 'is_active', 'date_joined', 'password')


class UsersUpdateModelForm(UserChangeForm):
    class Meta:
        model = Users
        exclude = ('created_at', 'updated_at', 'groups', 'user_permissions',
            'last_login', 'is_active', 'date_joined')

class UserCreationForm(UserCreationForm):
	class Meta:
		model = Users
		exclude = ('username', 'ci', 'first_name', 'last_name', 'email','is_secretaria','is_profesor','is_alumno')
