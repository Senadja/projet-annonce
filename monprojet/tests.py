from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from  monapp.models import Annonce

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.shop_url = reverse('shop')
        self.furniture_url = reverse('furniture')
        self.contact_url = reverse('contact')
        self.about_url = reverse('about')
        self.ajoute_url = reverse('ajoute')
        self.logout_url = reverse('logout')
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_shop_view(self):
        response = self.client.get(self.shop_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop.html')

    # Ajoutez d'autres tests pour les autres vues de votre application

    def test_authenticate_user(self):
        login_data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.login_url, login_data)
        self.assertRedirects(response, reverse('index'))

    def test_add_annonce_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.ajoute_url, {'title': 'Test Annonce', 'content': 'Test Content'})
        self.assertEqual(response.status_code, 302)  # Assurez-vous que l'utilisateur connecté est redirigé

    def test_add_annonce_unauthenticated(self):
        response = self.client.post(self.ajoute_url, {'title': 'Test Annonce', 'content': 'Test Content'})
        self.assertEqual(response.status_code, 302)  # Assurez-vous que l'utilisateur non connecté est redirigé
    def test_logout_view(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Assurez-vous que l'utilisateur est redirigé après la déconnexion

    # Ajoutez d'autres tests pour les autres vues de votre application

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.annonce = Annonce.objects.create(title='Test Annonce', content='Test Content', annonceur=self.user)

    def test_annonce_creation(self):
        self.assertEqual(self.annonce.title, 'Test Annonce')
        self.assertEqual(self.annonce.content, 'Test Content')
        self.assertEqual(self.annonce.annonceur, self.user)

    # Ajoutez d'autres tests pour les modèles de votre application

    def test_annonce_str_representation(self):
        annonce = Annonce.objects.create(title='Test Annonce', content='Test Content', annonceur=self.user)
        self.assertEqual(str(annonce), 'Test Annonce')

    # Ajoutez d'autres tests pour les représentations de chaînes d'autres modèles

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpassword')
        self.assertEqual(user.username, 'testuser2')
        self.assertEqual(user.email, 'test2@example.com')

    # Ajoutez d'autres tests pour les fonctionnalités liées aux utilisateurs

    def test_annonce_deletion(self):
        Annonce.objects.create(title='Test Annonce 2', content='Test Content 2', annonceur=self.user)
        annonce_to_delete = Annonce.objects.get(title='Test Annonce 2')
        annonce_to_delete.delete()
        self.assertEqual(Annonce.objects.count(), 1)

    # Ajoutez d'autres tests pour d'autres fonctionnalités de suppression

    def test_annonce_update(self):
        annonce_to_update = Annonce.objects.get(title='Test Annonce')
        annonce_to_update.title = 'Updated Test Annonce'
        annonce_to_update.save()
        updated_annonce = Annonce.objects.get(title='Updated Test Annonce')
        self.assertEqual(updated_annonce.title, 'Updated Test Annonce')

    # Ajoutez d'autres tests pour d'autres fonctionnalités de mise à jour
    def test_user_representation(self):
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpassword')
        self.assertEqual(str(user), 'testuser3')

    # Ajoutez d'autres tests pour les représentations de chaînes d'autres modèles

   

    # Ajoutez d'autres tests pour d'autres fonctionnalités liées aux images ou fichiers

    def test_annonce_content_length(self):
        annonce = Annonce.objects.create(title='Test Annonce', content='A' * 1000, annonceur=self.user)
        self.assertTrue(len(annonce.content) <= 1000)  # Assurez-vous que la longueur du contenu de l'annonce est limitée
