from urllib.parse import quote_plus # Share_string

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, ("Successfully Created"))
        return HttpResponseRedirect(instance.get_absolute_url())
    #if request.method == 'POST':
    context = {
        "form":form
    }
    return render(request, 'post_form.html', context)

def post_list(request): #list items
    today = timezone.now().date()
    queryset_list = Post.objects.active() #.order_by('-timestamp')
    #queryset_list = Post.objects.filter(draft=False).filter(publish__lte = timezone.now())
    if request.user.is_staff or  request.user.is_superuser:
        queryset_list = Post.objects.all()

    #search box list
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
        ).distinct()

    context = {
        'object_list':queryset_list,
        'title': 'List',
        'today':today,
    }
    return render(request, 'post_list.html', context)


def post_detail(request, slug=None):
    #instance= Post.objects.get(id=id)
    instance = get_object_or_404(Post, slug=slug)
    if instance.publish > timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {
        'title': instance.title,
        "instance": instance,
        "share_string": share_string,
        }
    return render(request, 'post_detail.html', context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    print(instance)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, ('Edit Successfully'))
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': instance.title,
        "instance": instance,
        "form":form
    }
    return render(request, 'post_form.html', context)

def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.info(request, ("Delete Successfully"))
    return redirect('posts:list')