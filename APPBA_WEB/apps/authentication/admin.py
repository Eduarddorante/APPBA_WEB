from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Users

# Register your models here.
# admin.site.register(Account)
@admin.register(Users)
class Users(UserAdmin):
    list_display = ('ci','is_director','is_secretaria_danza','is_secretaria_teatro','is_secretaria_musica','is_secretaria_artes','is_staff')
    list_filter = ('is_secretaria_danza','is_secretaria_teatro','is_secretaria_musica','is_secretaria_artes','is_director','is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'ci', 'first_name', 'last_name', 'email','is_secretaria_danza','is_secretaria_teatro','is_secretaria_musica','is_secretaria_artes','is_director','is_alumno')
    ordering = ('ci',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('ci', 'password')  }),
        (_('Personal info'), {'fields': ('ci', 'first_name', 'last_name', 'email','is_secretaria_danza','is_secretaria_teatro','is_secretaria_musica','is_secretaria_artes','is_director')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username' ,'ci', 'first_name', 'last_name', 'email','is_secretaria_danza','is_secretaria_teatro','is_secretaria_musica','is_secretaria_artes','is_director','password1', 'password2'),
        }),
    )