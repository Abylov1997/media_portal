from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.filters import ListFilter
from mediaportalapp.models import Category, Article, Comments, UserAccount

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Article, ArticleAdmin)
admin.site.register(UserAccount)