from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Post
from .forms import PostForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.


def index(request):
    return render(request, "index.html")


def posts(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "posts.html", {"posts": posts})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("posts")
    else:
        form = PostForm()
    return render(request, "post_form.html", {"form": form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("posts")
    else:
        form = PostForm(instance=post)
    return render(request, "post_form.html", {"form": form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id, user=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("posts")
    return render(request, "post_delete.html", {"post": post})


def register(request):
    if request.method == "POST":
        ureg_form = UserRegistrationForm(request.POST)
        if ureg_form.is_valid():
            user = ureg_form.save(commit=False)
            user.set_password(ureg_form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("posts")
    else:
        ureg_form = UserRegistrationForm()

    return render(request, "registration/register.html", {"form": ureg_form})
