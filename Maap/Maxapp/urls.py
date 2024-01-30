from django.urls import path
from . import views
from .views import HomeView, PostDetailView, NewPostView, EditPostView, DeletePostView




urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('newpost/', NewPostView.as_view(), name='newpost'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete'),
]
