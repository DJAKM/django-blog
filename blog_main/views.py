from django.shortcuts import render
from blogs.models import Category,Blog
def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True , status=1).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status=1)
    context = {
        'featured_posts': featured_posts,
        'posts': posts
    }
    return render(request,'home.html',context)