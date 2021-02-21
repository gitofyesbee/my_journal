from django.shortcuts import render, get_object_or_404
from .models import Post
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


class PostListView(generic.ListView):
    queryset = Post.published.all()
    template_name = 'blog/post/list.html'
    context_object_name = 'post_list'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(status="published")


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})