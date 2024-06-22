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

