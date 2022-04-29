from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group, User
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts_group.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    posts_count = posts.count()
    name = user.get_full_name()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'name': name,
        'posts': posts,
        'page_obj': page_obj,
        'posts_count': posts_count,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    related = Post.objects.select_related('author', 'group')
    post = related.get(pk=post_id)
    posts_count = related.filter(author=post.author).count()
    name = post.author.get_full_name()
    user = post.author
    context = {
        'user': user,
        'name': name,
        'related': related,
        'post': post,
        'posts_count': posts_count,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post_create = form.save(commit=False)
            post_create.author = request.user
            post_create.save()
            return redirect('posts:profile', post_create.author)
    context = {'form': form}
    return render(request, 'posts/create_post.html', context)


def post_edit(request, post_id):
    post = Post.objects.get(id=post_id)
    is_edit = True
    if post.author != request.user:
        return redirect('posts:post_detail', post_id)
    else:
        if request.method != 'POST':
            form = PostForm(instance=post)
        else:
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('posts:post_detail', post_id)
        context = {'form': form, 'is_edit': is_edit}
        return render(request, 'posts/create_post.html', context)
