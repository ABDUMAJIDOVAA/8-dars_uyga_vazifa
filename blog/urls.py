from django.urls import path
from .views import (all_posts, posts_by_category, post_detail, post_create, post_update, post_delete,
                    user_login, user_logout, user_register)


urlpatterns = [
    path('', all_posts, name='index'),
    path('category/<int:category_id>/', posts_by_category, name='bolim'),
    path('detail/<int:pk>/', post_detail, name='post_detail'),
    path('add/', post_create, name='post_create'),
    path('update/<int:pk>/', post_update, name='post_update'),
    path('delete/<int:pk>/', post_delete, name='post_delete'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
]

