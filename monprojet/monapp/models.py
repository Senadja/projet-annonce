from django.db import models
from django.contrib.auth.models import User

class Annonceur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Ajoutez d'autres champs spécifiques à l'annonceur au besoin

class Annonce(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    #is_approved = models.BooleanField(default=False)
    #approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    annonceur = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    def __str__(self):
        return self.title

class Commentaire(models.Model):
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"

