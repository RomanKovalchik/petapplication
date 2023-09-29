from django.shortcuts import render


# Create your views here.

# Create your views here.

def user(request):
    return render(request, '/user.html', {})

# Create your views here.


def login(request):
    return render(request, 'user/login.html', {})


def feedbacks(request):
    return render(request, 'user/feedbacks.html', {})


def logout(request):
    return render(request, 'user/logout.html', {})


def register(request):
    return render(request, 'user/register.html', {})


def user_history(request):
    return render(request, 'user/user_history.html', {})