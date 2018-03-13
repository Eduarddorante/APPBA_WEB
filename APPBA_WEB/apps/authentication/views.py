# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.context import RequestContext
from .forms import UsersModelForm, UsersUpdateModelForm
from ...apps.utils.mixins import AdminRequiredMixin,UsuarioRequiredMixin
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from ...apps.utils.mixins import AdminRequiredMixin,UsuarioRequiredMixin
from django.views.generic import TemplateView, View
# import mixins
from django.template.context import RequestContext
from django.conf import settings
from .models import Users
from ...apps.actividad.models import Actividad
from .forms import UsersModelForm, UsersUpdateModelForm
# mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# import class based views
from django.views.generic import View

# Create your views here.

class HomeTemplateView(LoginRequiredMixin,AdminRequiredMixin, ListView):
    context_object_name = 'listar_actividad'
    model = Actividad
    template_name = 'administrador/inicio_admin.html'

class LoginView(View):
    form_class = AuthenticationForm
    template_name = "login/page-login.html"
    mensaje = ""

    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login/page-login.html", { 'form': form , 'message': ''})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # redirect
                url_next = request.GET.get('next')
                if url_next is not None:
                    return redirect(url_next)
                else:
                    #return redirect(reverse_lazy('eventos:list'))
                    return render(request,'login/preloader.html')
            else:
                return HttpResponse("Inactive user.")
        else:
            mensaje ="Usuario o Contraseña Incorrecta."
        return render(request, self.template_name, {'form': self.form_class, 'message': mensaje})

class UsersCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Users
    form_class = UsersModelForm
    template_name = 'administrador/registro_secretarias.html'
    success_url = '/listado_secretarias/'
    
class UserListView(LoginRequiredMixin,AdminRequiredMixin, ListView):
    context_object_name = 'list_user'
    model = Users
    template_name = 'administrador/listado_secretarias.html'

class UserUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    template_name = 'administrador/registro_secretarias.html'
    model = Users
    fields = ['first_name','last_name','email','is_secretaria_danza','is_secretaria_teatro','is_secretaria_musica','is_secretaria_artes']
    success_url = '/listado_secretarias/'

class UserDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
    model = Users
    template_name = 'administrador/user_confirm_delete.html'
    success_url = reverse_lazy('aunth:list_user')       

# logout
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')