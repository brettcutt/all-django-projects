from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import BlogForm


def get_blogs(request):
    items = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "get_blogs.html", {'items': items})


def blog_detail(request, id):
    item = get_object_or_404(Post, id=id)
    item.views += 1
    item.save()

    return render(request, "blog_detail.html", {'item': item})


def create_or_edit_blog(request, id=None):
    post = get_object_or_404(Post, id=id) if id else None
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(blog_detail, post.id)

    else:
        form = BlogForm(instance=post)
    return render(request, "blog_form.html", {'form': form})


"""
# Adding a blog
def blog_form(request):
    if request.method == 'POST':

        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = BlogForm()

    return render(request, "blog_form.html", {"form": form})
"""
"""
# editing a blog
def edit_blog(request, id):
    item = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect(blogs)

    else:
        form = BlogForm(instance=item)
    return render(request, "blog_form.html", {'form': form})
"""
