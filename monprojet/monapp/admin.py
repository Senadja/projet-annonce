from django.contrib import admin
from .models import Annonce, Annonceur, Commentaire
from django.contrib.auth.models import User
from .models import Article, Comment
admin.site.register(Annonce)
admin.site.register(Annonceur)
admin.site.register(Commentaire)
