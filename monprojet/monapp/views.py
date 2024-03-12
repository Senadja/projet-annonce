from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Article, Comment, Annonce, Annonceur
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from datetime import date,timedelta,datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    datas={
    
    }
    return render(request, 'index.html', datas)

def shop(request):
    annonces = Annonce.objects.all()
    today_plus_one_week = datetime.now().date()
    print(today_plus_one_week)
    datas={
        'annonces' : annonces,
        'today_plus_one_week': today_plus_one_week,
    }
    return render(request, 'shop.html', datas)

from .models import Article  # Assurez-vous d'importer le modèle Article

def furniture(request):
    articles = Article.objects.all()  # Récupérez tous les articles depuis la base de données
    return render(request, 'furniture.html', {'articles': articles})  # Passez les articles au modèle

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

@login_required  # Assurez-vous que l'utilisateur est connecté avant d'ajouter une annonce
def ajoute(request):
    user = request.user
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        # Récupérez le fichier image à partir de request.FILES au lieu de request.POST
        image = request.FILES.get("image")
        annonce = Annonce(title=title, content=content, image=image, annonceur=user)
        annonce.save() 
        # Redirigez l'utilisateur vers la page d'accueil ou une autre page après l'ajout de l'annonce
        return redirect('index')
    else:
        # Si l'utilisateur n'est pas connecté, redirigez-le vers la page de connexion avec un message d'erreur
        if not request.user.is_authenticated:
            messages.error(request, 'Vous devez être connecté pour accéder à cette page.')
            return redirect('login')
        else:
            return render(request, 'ajoute.html')

def auth(request):
    if request.method == "POST":
        if 'inscription' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirmpwd = request.POST['comfirmpwd']
            if User.objects.filter(username=username):
                messages.error(request, "nom d'utilisateur déjà pris, veuillez en essayer un autre.")
                return redirect('login')
            if User.objects.filter(email=email):
                messages.error(request, 'Cet email a un compte.')
                return redirect('login')
            if len(username)>10:
                messages.error(request, "S'il vous plaît, le nom d'utilisateur ne doit pas contenir plus de 10 caractères.'")
                return redirect('login')
            if len(username)<5:
                messages.error(request, "S'il vous plaît, le nom d'utilisateur doit contenir au moins 5 caractères.")
                return redirect('login')
            if not username.isalnum():
                messages.error(request, "le nom d'utilisateur doit être alphanumérique.")
                return redirect('login')
            if password != confirmpwd:
                messages.error(request, 'Le mot de passe ne correspond pas!')  
                return redirect('login')  
            try:
                validate_password(password)
            except ValidationError as e:
                # Gérer les erreurs de validation du mot de passe
                messages.error(request, e)
                return redirect('login')
            
            my_user = User.objects.create_user(username, email, password)
            my_user.is_active = True
            my_user.save()
            
            user = authenticate(username=username,password=password)
            if user is not None and user.is_active:
                login(request,user)
                #### redirection si les infos sont correctes
                return redirect('index')
        elif 'connexion' in request.POST:
            name = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=name,password=password)
            if user is not None and user.is_active:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe invalide')
                return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

# def add_article(request):
#     if request.method == 'POST':
#         form = Article.Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('article_list')
#     else:
#         form = ArticleForm()
#     return render(request, 'add_article.html', {'form': form})

def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('article_list')

# def add_comment(request, article_id):
#     article = Article.objects.get(id=article_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.article = article
#             comment.save()
#             return redirect('article_list')
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment.html', {'form': form})

