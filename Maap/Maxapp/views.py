from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Fileupload
from .forms import PostForm, EditForm, FileForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

# Create your views here.
#def home(request):
    #return render(request, 'home.html',{})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['id']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'

class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'newpost.html'
    #fields = ('title','author','body')

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit.html'
    #fields = ('title','body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

def files_uploaded(request):
    files = Fileupload.objects.all()
    ordering = ['id']
    return render(request, 'files_uploaded.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {'form': form})