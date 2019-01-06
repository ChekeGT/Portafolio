from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'