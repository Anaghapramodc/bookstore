from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('booklist')

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
