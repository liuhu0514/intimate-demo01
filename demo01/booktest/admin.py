from django.contrib import admin
from .models import BookInfo, HeroInfo
# Register your models here.


class HeroInfoInlines(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['num', 'title', 'pub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 5
    inlines = [HeroInfoInlines]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['num', 'name', 'sex', 'content', 'book']
    list_filter = ['hname', 'hgender', 'hcontent', 'hbook']
    search_fields = ['hname', 'hcontent', 'hbook']
    list_per_page = 5


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

"""
通过少量的代码实现强大的后台管理 
"""
