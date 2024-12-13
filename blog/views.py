from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm, CreateBlogForm, EditBlogForm, EditCommentForm
from .models import Blog, Comment


def home_view(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'index.html', context)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


def logout_view(request):
    logout(request)
    return redirect('home')


def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


def user_blogs_view(request):
    user = request.user
    blogs = Blog.objects.filter(author=user)
    context = {'blogs': blogs}
    return render(request, 'user_blogs.html', context)


def create_blog_view(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('user-blogs')
    else:
        form = CreateBlogForm()
    return render(request, 'create_blog.html', {'form': form})


def edit_blog_view(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = EditBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', id=blog.id)
    else:
        form = EditBlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form})


def blog_detail_view(request, id):
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        comment = Comment(blog=blog, author=request.user, content=comment)
        comment.save()
        return redirect('blog-detail', id=id)
    context = {'blog': blog, 'comments': comments}
    return render(request, 'blog_detail.html', context)



def edit_comment_view(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', id=comment.blog.id)
    else:
        form = EditCommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})


def delete_comment_view(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('blog-detail', id=comment.blog.id)



