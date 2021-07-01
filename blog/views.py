from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm
from comments.models import Comment
from comments.forms import CommentForm

# Create your views here.

def hub(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = int(request.GET.get('page',1))
    blogs = paginator.page(page)
    return render(request, 'home.html', {'blogs':blogs})

def home(request):
    blogs = Blog.objects.filter(community="C1")
    paginator = Paginator(blogs, 3)
    page = int(request.GET.get('page',1))
    blogs = paginator.page(page)
    return render(request, 'home.html', {'blogs':blogs})

def home2(request):
    blogs = Blog.objects.filter(community="C2")
    paginator = Paginator(blogs, 3)
    page = int(request.GET.get('page',1))
    blogs = paginator.page(page)
    return render(request, 'home2.html', {'blogs':blogs})

def home3(request):
    blogs = Blog.objects.filter(community="C3")
    paginator = Paginator(blogs, 3)
    page = int(request.GET.get('page',1))
    blogs = paginator.page(page)
    return render(request, 'home3.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        comment_form.instance.author_id = request.user.id
        comment_form.instance.document_id = id
        if comment_form.is_valid():
            comment = comment_form.save()


    #models.py에서 document의 related_name을 comments로 해놓았다.

    comment_form = CommentForm()
    comments = Blog.objects.get(id=id).comments.all()
    print(type(comments))
    return render(request, 'detail.html', {'blog':blog, "comments":comments, "comment_form":comment_form})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('blog:detail', new_blog.id )
    return redirect('blog:home')

def edit(request,id):
    edit_blog = Blog.objects.get(id= id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog = Blog.objects.get(id= id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body'] #name 그대로
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('blog:detail', update_blog.id )

def delete(request,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('blog:home')

def comment_delete(request,id):
    delete_comment = Comment.objects.get(id=id)
    blog_id = delete_comment.document.id
    delete_comment.delete()
    return redirect('blog:detail', blog_id)

def search(request):
    blogs = Blog.objects.filter(writer=request.GET["searcher"])
    paginator = Paginator(blogs, 3)
    page = int(request.GET.get('page',1))
    blogs = paginator.page(page)
    return render(request, 'home.html', {'blogs':blogs})