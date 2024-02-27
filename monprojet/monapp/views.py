from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Article, Comment, Annonce, Annonceur

# Create your views here.

def index(request):
    datas={
    
    }
    return render(request, 'index.html', datas)

def shop(request):
    return render(request, 'shop.html')

def furniture(request):
    return render(request, 'furniture.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def ajoute(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.POST.get("image")
        annonce = Annonce(title=title, content=content, image=image, annonceur=user)
        annonce.save() 
    return render(request, 'ajoute.html')

def auth (request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("pass")
        user = authenticate(username=name,password=password)
        if user is not None and user.is_active:
            login(request,user)
            
            #### redirection si les infos sont correctes
            return redirect('index')
        else:
            print("login échoué")
           # message = "Merci de vérifiez vos informations"

    

    return render(request, 'login.html')



def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

#def add_article(request):
    if request.method == 'POST':
        form = Article.Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('article_list')

#def add_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_list')
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})


