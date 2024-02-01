from django.urls import path
from . import views
from .views import HomeView, PostDetailView, NewPostView, EditPostView, DeletePostView, FileForm, Fileupload
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from Maxapp import views 
from django.contrib.auth import logout



urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post'),
    path('newpost/', NewPostView.as_view(), name='newpost'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete'),
    path('fileupload/', views.upload_file, name='fileupload'),
    path('files/', views.files_uploaded, name='files'),
    path('uploads/', views.Filelist.as_view(), name='upload'),
    path('files/<int:pk>/', views.delete_file, name='delete_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)