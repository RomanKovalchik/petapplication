from  django.urls import path

from . import views

urlpatterns = [
#endpoints for blog app
    path('index', views.index, name='index'),
    path('<int:post_id>', views.blog_post, name='post'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
]