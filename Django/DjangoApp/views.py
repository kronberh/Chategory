from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseNotFound
from .models import User, Category, Post, Comment
from .forms import RegisterForm, CategoryForm, PostForm, CommentForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, "registration/register.html", context)

def user(request, username:str):
    user = User.objects.filter(username=username).first()
    if user == None:
        return HttpResponseNotFound()
    context = {
        'user': user,
        'is_profile': user == request.user
    }
    return render(request, 'user.html', context)

def index(request):
    categories = Category.objects.annotate(post_count=Count('categoryPosts'))
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)

@login_required
def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.author = request.user
            category.save()
            return redirect(f'/categories/{category.id}')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'add_category.html', context)

def category(request, id:int):
    category = Category.objects.filter(id=id).first()
    if category == None:
        return HttpResponseNotFound()
    posts = category.categoryPosts.all()
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'category.html', context)

@login_required
def addPost(request, category_id:int):
    category = Category.objects.filter(id=category_id).first()
    if category == None:
        return HttpResponseNotFound()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category = category
            post.save()
            return redirect(f'/categories/{category_id}/posts/{post.id}')
    else:
        form = PostForm()
    context = {
        'category': category,
        'form': form
    }
    return render(request, 'add_post.html', context)

def post(request, category_id:int, post_id:int):
    post = Post.objects.filter(id=post_id).first()
    if post == None or post.category.id != category_id:
        return HttpResponseNotFound()
    comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post.html', context)

@login_required
def addComment(request, category_id:int, post_id:int):
    post = Post.objects.filter(id=post_id).first()
    if post == None or post.category.id != category_id:
        return HttpResponseNotFound()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(f'/categories/{category_id}/posts/{post.id}',)
    else:
        form = CommentForm()
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'add_comment.html', context)

@login_required
def addReply(request, category_id:int, post_id:int, comment_id:int):
    comment = Comment.objects.filter(id=comment_id).first()
    if comment == None or comment.post.id != post_id or comment.post.category.id != category_id:
        return HttpResponseNotFound()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.post = comment.post
            reply.answered = comment
            reply.save()
            return redirect(f'/categories/{category_id}/posts/{comment.post.id}')
    else:
        form = CommentForm()
    context = {
        'form': form,
        'comment': comment
    }
    return render(request, 'add_reply.html', context)

@login_required
def likePost(request, category_id:int, post_id:int):
    post = Post.objects.filter(id=post_id).first()
    if post == None or post.category.id != category_id:
        return HttpResponseNotFound()
    if post.is_liked_by(request.user):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(f'/categories/{category_id}/posts/{post_id}')

@login_required
def likeComment(request, category_id:int, post_id:int, comment_id:int):
    comment = Comment.objects.filter(id=comment_id).first()
    if comment == None or comment.post.id != post_id or comment.post.category.id != category_id:
        return HttpResponseNotFound()
    if comment.is_liked_by(request.user):
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
    return redirect(f'/categories/{category_id}/posts/{post_id}')
