from datetime import date
from django.shortcuts import render

#temp dumby data will soon come from database
all_posts = [
    {
        "slug": "tesla-star-wars",
        "image": "tesla.jpg",
        "author": "Jake",
        "date": date(2023, 7, 10),
        "title": "Tesla",
        "excerpt": "Incididunt velit dolore veniam veniam in incididunt laborum officia enim sunt eu aliquip officia. Laboris officia veniam eu dolore deserunt in in laboris irure ullamco velit reprehenderit minim. Adipisicing incididunt anim deserunt velit.",
        "content": """Laboris in quis incididunt quis. Aliquip mollit magna do esse magna veniam ad officia ut exercitation ad irure. 
            Dolor est sit dolor ad nisi sunt amet exercitation nostrud.

            Amet nulla sit esse nostrud pariatur. Eu nostrud incididunt dolore ut ex minim anim nulla aute aliqua reprehenderit dolor Lorem nisi. 
            Eu ad cupidatat sunt non sunt esse occaecat.
        """
    },
    {
        "slug": "tar-wars",
        "image": "starwars.jpg",
        "author": "Jake",
        "date": date(2023, 7, 9),
        "title": "Star Wars",
        "excerpt": "Incididunt velit dolore veniam veniam in incididunt laborum officia enim sunt eu aliquip officia. Laboris officia veniam eu dolore deserunt in in laboris irure ullamco velit reprehenderit minim. Adipisicing incididunt anim deserunt velit.",
        "content": """Laboris in quis incididunt quis. Aliquip mollit magna do esse magna veniam ad officia ut exercitation ad irure. 
            Dolor est sit dolor ad nisi sunt amet exercitation nostrud.

            Amet nulla sit esse nostrud pariatur. Eu nostrud incididunt dolore ut ex minim anim nulla aute aliqua reprehenderit dolor Lorem nisi. 
            Eu ad cupidatat sunt non sunt esse occaecat.
        """
    },
    {
        "slug": "space-x-dragon",
        "image": "spacex.png",
        "author": "Jake",
        "date": date(2023, 7, 8),
        "title": "Space X Dragon Capsule",
        "excerpt": "Incididunt velit dolore veniam veniam in incididunt laborum officia enim sunt eu aliquip officia. Laboris officia veniam eu dolore deserunt in in laboris irure ullamco velit reprehenderit minim. Adipisicing incididunt anim deserunt velit.",
        "content": """Laboris in quis incididunt quis. Aliquip mollit magna do esse magna veniam ad officia ut exercitation ad irure. 
            Dolor est sit dolor ad nisi sunt amet exercitation nostrud.

            Amet nulla sit esse nostrud pariatur. Eu nostrud incididunt dolore ut ex minim anim nulla aute aliqua reprehenderit dolor Lorem nisi. 
            Eu ad cupidatat sunt non sunt esse occaecat.
        """
    }
]

def get_date(post):
    return post['date']


# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)

    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    id_post = next(post for post in all_posts if post['slug'] == slug)

    return render(request, "blog/post-detail.html", {
        "post": id_post
    })