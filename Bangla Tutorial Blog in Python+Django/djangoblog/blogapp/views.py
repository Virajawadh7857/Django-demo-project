from django.shortcuts import render,HttpResponse, get_object_or_404,redirect,Http404
from . models import author, category, article,comment
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import createForm,registerUserform,createAuthor,commentForm,categoryForm
from django.contrib import messages


# Create your views here.
def index(request):
    post = article.objects.all()
    serach = request.GET.get('q')
    if serach:
        post = post.filter(
            Q(title__icontains=serach)|
            Q(body__icontains=serach)
        )
    paginator = Paginator(post, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    total_article = paginator.get_page(page)
    context ={
        "post": total_article
    }
    return render(request, "index.html", context)

def getauthor(request,name):
    post_author=get_object_or_404(User, username=name)
    auth=get_object_or_404(author, name=post_author.id)
    post=article.objects.filter(article_author=auth.id)
    context={
        "auth": auth,
        "post": post
    }
    return render(request, "profile.html", context)

def getsingle(request,id):
    post = get_object_or_404(article, pk=id)
    first = article.objects.first()
    last = article.objects.last()
    related = article.objects.filter(category =post.category).exclude(id=id)[:4]
    getComment = comment.objects.filter(post=id)
    form = commentForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=post
        instance.save()
    context={
        "post":post,
        "first":first,
        "last":last,
        "related":related,
        "form":form,
        "comment":getComment
    }
    return render(request, "single.html",context)

def getTopic(request,name):
    cat = get_object_or_404(category, name=name)
    post=article.objects.filter(category=cat.id)
    return render(request, "category.html", {"post":post, "cat":cat})

def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('blog:index')
            else:
                messages.add_message(request, messages.ERROR, 'Username or Password mismatch')
                return render(request,"login.html")
    return render(request, "login.html")

def getLogout(request):
    logout(request)
    return redirect('blog:index')

def getCreate(request):
    if request.user.is_authenticated:
        u=get_object_or_404(author,name=request.user.id)
        form = createForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=u
            instance.save()
            return redirect('profile')
        return render(request, 'create.html', {"form": form})
    else:
        return redirect('login')


def getProfile(request):
    if request.user.is_authenticated:
        user=get_object_or_404(User, id=request.user.id)
        author_profile = author.objects.filter(name=user.id)
        if author_profile:
            authorUser = get_object_or_404(author, name=request.user.id)
            post = article.objects.filter(article_author=authorUser.id)
            return render(request, "logged_in_profile.html", {"post":post, "user":authorUser})
        else:
            form = createAuthor(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.name=user
                instance.save()
                return redirect('profile')
            return render(request, "crateauthor.html", {"form":form})
    else:
        return redirect('login')

def getUpdate(request,pid):
    if request.user.is_authenticated:
        u=get_object_or_404(author,name=request.user.id)
        post = get_object_or_404(article, id=pid)
        form = createForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.article_author=u
            instance.save()
            messages.success(request, 'Article is updated successfully.')
            return redirect('profile')
        return render(request, 'create.html', {"form": form})
    else:
        return redirect('login')


def getDelete(request,pid):
    if request.user.is_authenticated:
        post = get_object_or_404(article, id=pid)
        post.delete()
        messages.warning(request, 'Article is Deleted successfully.')
        return redirect('profile')
    else:
        return redirect('login')

def getRegister(request):
    form = registerUserform(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request, 'Registeration successfully completed.')
        return redirect('login')
    return render(request,"register.html", {"form":form})

def getCategory(request):
    query = category.objects.all()
    return render(request,"topics.html",{"topic":query})

def createTopic(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            form = categoryForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Topic is Created!')
                return redirect('blog:category')
            else:
                return render(request, "create_topics.html", {"form": form})
        else:
            raise Http404("You can't access this page !")
    else:
        return redirect('blog:login')


"""from django.shortcuts import (
render_to_response
)
from django.template import RequestContext

# HTTP Error 400

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response"""