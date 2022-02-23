from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User


from users.forms import SignupForm

#from posts.models import Post
from users.models import Profile



class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)


class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View."""


class UserDetailView(DetailView):
    """User detail view."""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username_slug'
    queryset = User.objects.all()
    context_object_name = 'user'

 

