from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.
def AllBlogView(request):
    qs=Post.objects.all()
    return render(request,"Allblogs.html",{"qs": qs,})

def HomeView(request):
    return render(request,"base.html",{})

def BlogView(request,my_id):
    obj=Post.objects.get(pk=my_id);
    if(obj):
       return  render(request,"blog.html",{"obj":obj})
    else:
        return HttpResponse("The pasge requested is deleted")