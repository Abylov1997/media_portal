"""mp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from mediaportalapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', CategoryListView.as_view(), name='base_view'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^user_account_(?P<user>[-\w]+)/$', UserAccountView.as_view(), name='account_view'),
    url(r'^show_article_image/$', DynamicArticleImageView.as_view(), name='article_image'),
    url(r'^add_comment/$', CreateCommentView.as_view(), name='add_comment'),
    url(r'^display_articles_by_category/$', DisplayArticlesByCategoryView.as_view(), name='articles_by_category'),
    url(r'^user_reaction/$', UserReactionView.as_view(), name='user_reaction'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    url(r'^login/$', LoginView.as_view(), name='login_view'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('base_view')), name='logout_view'),
    url(r'^add_to_favorites/$', AddArticleToFavorites.as_view(), name='add_to_favorites'),
    url(r'^delete_to_favorites/$', DeleteArticleFromFavorites.as_view(), name='delete_to_favorites'),
    url(r'^search/$', SearchView.as_view(), name='search_view')
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)