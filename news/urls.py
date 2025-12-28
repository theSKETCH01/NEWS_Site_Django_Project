from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('category/<str:category>/', category_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('add/', add_news),
    path('my-news/', my_news),
    path('edit/<int:news_id>/', edit_news),
    path('delete/<int:news_id>/', delete_news),
    path('register/', register_view),
]