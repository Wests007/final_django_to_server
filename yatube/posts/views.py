from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required

from .models import Follow, Post, Group, User
from .forms import PostForm, CommentForm
from .utils import get_page_paginator


# @cache_page(20)
def index(request):
    """View-функция для главной страницы"""

    template = 'posts/index.html'
    text = 'Это главная страница проекта TravelTube'
    post_list = Post.objects.select_related('group')
    page_obj = get_page_paginator(request, post_list, Post.LIMIT_POST)
    user=request.user
    context = {
        'text': text,
        'page_obj': page_obj,
        'user': user,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """View-функция для страницы сообщества"""

    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    page_obj = get_page_paginator(request, posts, Post.LIMIT_POST)
    user=request.user
    context = {
        'group': group,
        'page_obj': page_obj,
        'user': user,
    }
    return render(request, template, context)


def profile(request, username):
    """View-функция для страницы профайла"""

    template = 'posts/profile.html'
    author = get_object_or_404(User, username=username)
    posts = author.posts.all().select_related('group')
    page_obj = get_page_paginator(request, posts, Post.LIMIT_POST)
    following = (
        request.user.is_authenticated
        and author.following.filter(user=request.user).exists()
    )
    user=request.user
    context = {
        'author': author,
        'page_obj': page_obj,
        'following': following,
        'user': user,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    """View-функция для страницы отдельного поста"""

    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.GET or None)
    comments = post.comments.all().select_related('author')
    user=request.user
    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'user': user,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    """View-функция для страницы создания поста"""

    template = 'posts/create_post.html'
    form = PostForm(
        request.POST or None,
        files=request.FILES or None
    )
    context = {
        'form': form,
    }
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', request.user.username)
    return render(request, template, context)


@login_required
def post_edit(request, post_id):
    """View-функция для страницы редактирования поста"""

    template = 'posts/create_post.html'
    post = get_object_or_404(Post, id=post_id)
    is_edit = True
    if request.user == post.author:
        form = PostForm(
            request.POST or None,
            files=request.FILES or None,
            instance=post
        )
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_id=post_id)
        context = {
            'form': form,
            'is_edit': is_edit,
        }
        return render(request, template, context)
    return redirect('posts:post_detail', post_id=post_id)


@login_required
def add_comment(request, post_id):
    """View-функция для страницы добавления комментария к посту"""

    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


@login_required
def follow_index(request):
    """View-функция для страницы постов по подписке"""

    text = 'Посты авторов по подписке'
    template = 'posts/follow.html'
    follow_posts = Post.objects.filter(author__following__user=request.user)
    page_obj = get_page_paginator(request, follow_posts, Post.LIMIT_POST)
    user=request.user
    context = {
        'page_obj': page_obj,
        'text': text,
        'user': user,
    }
    return render(request, template, context)


@login_required
def profile_follow(request, username):
    """View-функция для подписки на автора"""

    user = request.user
    author = User.objects.get(username=username)
    if user != author:
        Follow.objects.get_or_create(user=user, author=author)
    return redirect('posts:profile', username=author.username)


@login_required
def profile_unfollow(request, username):
    """View-функция для отписки от автора"""

    Follow.objects.filter(
        user=request.user,
        author__username=username
    ).delete()
    return redirect('posts:profile', username=username)
