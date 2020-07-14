from django.shortcuts import render, get_object_or_404
# from django.views import generic
from .models import Blog

# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    # blogs.order_by(Blog.objects.pub_date)
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id) #get_object_or_404(Model, pk(primary key))
    return render(request, 'blog/detail.html', {'blog': detailblog})

# class BlogOrder(generic.ListView):
#     queryset = Blog.objects.order_by('pub_date')
#     template_name = 'blog/allblogs.html'

