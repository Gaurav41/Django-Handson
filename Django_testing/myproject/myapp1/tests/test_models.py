from django.test import TestCase
from myapp1.models import Post, Product
from django.contrib.auth.models import User

class  TestAppModels(TestCase):

    def setUp(self):
        print("setup method runs before each test case")
        self.test_user1 = User.objects.create(username="testuser1",password="test")
        self.test_user2 = User.objects.create(username="testuser2",password="test")

    def test_post_model_str(self):
        title = Post(title="My First Post")
        title.save()
        self.assertEqual(str(title),"My First Post")

    def test_post_likes(self):
        
        title = Post.objects.create(title="My new Post",content="some temp text")
        title.likes.set([self.test_user1.pk,self.test_user2.pk])
        post = Post.objects.get(title="My new Post")
        self.assertEqual(post.likes.count(),2)

    