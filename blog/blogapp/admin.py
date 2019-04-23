from django.contrib import admin
from .models import Classify, Article, User, Label, Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'c_content', 'c_pub', 'c_www', 'c_email', 'c_article']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'a_title', 'a_abstract', 'a_content', 'a_pub_time', 'a_num', 'a_author', 'a_cls', 'a_label']


class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


class ClassifyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', ]


admin.site.register(User, UserAdmin)
admin.site.register(Classify, ClassifyAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

