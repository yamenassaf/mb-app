from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
	def setUp(self):
		Post.objects.create(text='just a test')

	def test_(self):
		post = Post.objects.get(id=1)
		self.assertEqual(post.text,'just a test')

class HomePageViewTest(TestCase):
	def test_url_by_locaion(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code,200)

	def test_url_by_name(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code,200)
		
	def test_template_used(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'home.html')