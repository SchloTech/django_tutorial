from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": Post.objects.all().order_by("-date")
    })

def post_detail(request, slug):
    id_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": id_post,
        "post_tags": id_post.tags.all()
    })