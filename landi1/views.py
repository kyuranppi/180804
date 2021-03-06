from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('-id')
    return render(request, 'landi1/post_list.html', {'posts': posts}) 

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'landi1/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'landi1/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'landi1/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def post_others(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    posts = Post.objects.all().order_by('-id')
    return render(request, 'landi1/other_diary.html', {'posts': posts})

@login_required
def scrap_list(request):
    posts = Post.objects.filter(scraped_date__isnull=False).order_by('published_date')
    posts = Post.objects.all().order_by('-id')
    return render(request, 'landi1/post_scrap.html', {'posts': posts})

@login_required
def post_scrap(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.scrap()
    return redirect('post_detail', pk=pk)




