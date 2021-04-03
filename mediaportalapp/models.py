from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Category(models.Model):
	"""Модель категорий"""

	name = models.CharField(max_length=50)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category-detail', kwargs={'slug': self.slug})


def generate_filename(instance, filename):
	"""Создание имени файла"""

	filename = instance.slug + '.jpg'
	return "{0}/{1}".format(instance.slug, filename)


class ArticleManager(models.Manager):
	"""Менеджер article"""

	def all(self, *args, **kwargs):
		return super(ArticleManager, self).get_queryset().filter(pk__in=[1,2,3])


class Article(models.Model):
	"""Модель новостей"""

	category = models.ForeignKey(Category)
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	image = models.ImageField(upload_to=generate_filename)
	content = models.TextField()
	likes = models.PositiveIntegerField(default=0)
	dislikes = models.PositiveIntegerField(default=0)
	comments = GenericRelation('comments')
	users_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
	objects = models.Manager()
	custom = ArticleManager()

	def __str__(self):
		return "Статья '{0}' из категории '{1}'".format(self.title, self.category.name)

	def get_absolute_url(self):
		return reverse('article-detail', kwargs={'category': self.category.slug, 'slug': self.slug})


class Comments(models.Model):
	"""Модель комментариев"""

	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	comment = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')


class UserAccount(models.Model):
	"""Модель аккаунта пользователя"""

	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email = models.EmailField(blank=True)
	favorite_articles = models.ManyToManyField(Article, blank=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('account_view', kwargs={'user': self.user.username})