from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User
from .forms import PostForm


def get_page_context(queryset, request):
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    posts = Post.objects.all()
    page_obj = get_page_context(posts, request)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts_group.all()
    page_obj = get_page_context(posts, request)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author)
    posts_count = posts.count()
    name = author.get_full_name()
    page_obj = get_page_context(posts, request)
    context = {
        'author': author,
        'name': name,
        'posts': posts,
        'posts_count': posts_count,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    related = Post.objects.select_related('author', 'group')
    post = related.get(pk=post_id)
    posts_count = related.filter(author=post.author).count()
    name = post.author.get_full_name()
    context = {
        'name': name,
        'related': related,
        'post': post,
        'posts_count': posts_count,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post_create = form.save(commit=False)
        post_create.author = request.user
        post_create.save()
        return redirect('posts:profile', post_create.author)
    context = {'form': form}
    return render(request, 'posts/create_post.html', context)


def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id)
    else:
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', post_id)
        context = {'form': form, 'is_edit': True}
        return render(request, 'posts/create_post.html', context)
