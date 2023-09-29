from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'blog/index.html', context={'name': 'Roman', 'lastname':'Kovalchik'})


def blog_post(request):
    return render(request, 'blog/post.html', {})


def feedbacks(request):
    return render(request, 'blog/feedbacks.html', {})
