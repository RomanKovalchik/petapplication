from  django.urls import path

from . import views


urlpatterns = [
#endpoints for blog app
    path('', views.user, name='user'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='feedbacks'),
    path('register', views.register, name='register'),
    path('user/history', views.user_history, name='user_history'),
]