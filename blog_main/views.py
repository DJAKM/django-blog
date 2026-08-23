from django.shortcuts import render
from blogs.models import Category,Blog
from aboutAndSocialLink.models import About
def home(request):
    featured_posts = Blog.objects.filter(is_featured=True , status=1).order_by('updated_at')
    try:
        about = About.objects.get()
    except:
        about = None
    posts = Blog.objects.filter(is_featured=False, status=1)
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about
    }
    return render(request,'home.html',context)