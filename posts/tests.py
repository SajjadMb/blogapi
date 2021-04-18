from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class blogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(
            'testuser',
            password= '1234'
        )
        test_user1.save()

        blog_post = Post.objects.create(
            author = test_user1,
            title = 'blog title',
            body = 'body content'
        )
        blog_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id = 1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'blog title')
        self.assertEqual(body, 'body content')
