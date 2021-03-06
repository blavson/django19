from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def post_list(request):
    queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                                            Q(title__icontains=query) |
                                            Q(content__icontains=query)
                                            )

    paginator = Paginator(queryset_list, 10)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    return render(request, 'post_list.html', {'posts' : queryset})

def post_detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    context = { 'title' :  instance.title,
                "instance" : instance
                }
    return render(request, 'post_detail.html', context)


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author =request.user
            instance.save()
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

@login_required
def post_update(request, slug):
    instance = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
        messages.success(request, "Successfully Updated")
        return redirect("posts:homepage")
    else:
        form  = PostForm(instance=instance)
        context = { 'title' :  instance.title,
                "instance" : instance,
                "form" : form,
                "button_title" : "Edit Post"
                }
    return render(request, 'post_form.html', context)

@login_required
def post_delete(request,slug):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Item  deleted")
    return redirect("posts:homepage")
