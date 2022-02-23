from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from posts.forms import PostForm


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        """Add User and profile to context. dictionary"""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()
    context_object_name = 'post'
