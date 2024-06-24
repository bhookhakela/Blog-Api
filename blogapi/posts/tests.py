from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class blogtest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1= User.objects.create_user(username='testuser1',password='test123')
        testuser1.save()
        # Create a blog post
        test_post=Post.objects.create(author=testuser1,title='test post',body='test')
        test_post.save()
    def test_blog_content(self):
        post=Post.objects.get(id=1)
        author=str(post.author)
        title=str(post.title)
        body=str(post.body)
        self.assertEqual(author,'testuser1')
        self.assertEqual(title,'test post')
        self.assertEqual(body,'test')

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Post

class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post1 = Post.objects.create(title='Post 1', body='Body 1', author=self.user)
        self.post2 = Post.objects.create(title='Post 2', body='Body 2', author=self.user)

    def test_post_list_unauthenticated(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post_list_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post_detail_unauthenticated(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_detail_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_unauthenticated(self):
        response = self.client.post(reverse('post-list'), {'title': 'Post 3', 'body': 'Body 3', 'author': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_create_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('post-list'), {'title': 'Post 3', 'body': 'Body 3', 'author': self.user.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)