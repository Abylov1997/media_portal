from django.views.generic.list import MultipleObjectMixin
from mediaportalapp.models import Category, Article

class CategoryAndArticlesListMixin(MultipleObjectMixin):
	"""Миксин category, articles"""

	def get_context_data(self, *args, **kwargs):
		context = {}
		context['categories'] = Category.objects.all()
		context['tab_articles'] = Article.objects.all()
		return context