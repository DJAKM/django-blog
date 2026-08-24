from django.shortcuts import render,redirect 
from blogs.models import Category,Blog
from aboutAndSocialLink.models import About
from .forms import RegistrationForm
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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context={
        'form' : form,
    }
    return render(request,'register.html',context)