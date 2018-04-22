from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm


def post_list(request):
    queryset = Post.objects.all().order_by('-updated')
    return render(request, 'post_list.html', {'posts' : queryset})

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = { 'title' :  instance.title,
                "instance" : instance
                }
    return render(request, 'post_detail.html', context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully created")
            return redirect("posts:homepage")
        else:
            messages.error("Message creation failed")
    else:
        form = PostForm()
    context = { "form":form ,
                    "button_title" : "New Post"
                    }
    return render(request, 'post_form.html', context)

def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance= instance)
        if form.is_valid():
            form.save()
        messages.success(request, "Successfully Updated")
        return redirect("posts:homepage")
    else:
        form  = PostForm(request.POST or None, instance=instance)
        context = { 'title' :  instance.title,
                "instance" : instance,
                "form" : form,
                "button_title" : "Edit Post"
                }
    return render(request, 'post_form.html', context)

def post_delete(request,id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Item  deleted")
    return redirect("posts:homepage")