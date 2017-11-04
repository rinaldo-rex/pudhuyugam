from django.contrib import admin
from .models import Idea, Issue,Article
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

admin.site.register(Idea)
admin.site.register(Issue)
admin.site.register(Article, MarkdownxModelAdmin)