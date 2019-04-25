from django.contrib import admin
from .models import User, Classify, Label, Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'a_title', 'a_abstract', 'a_content', 'a_pub_time',
                    'a_modify_time', 'a_num', 'a_author', 'a_cls', 'a_label', ]


class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'lname']


class ClassifyAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', ]


admin.site.register(User, UserAdmin)
admin.site.register(Classify, ClassifyAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Article, ArticleAdmin)
