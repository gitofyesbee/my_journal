from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'blog'
urlpatterns = [
    # post views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
]
