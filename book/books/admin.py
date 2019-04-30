from django.contrib import admin
from .models import StuUser, BookInfo, History, HotPic

# Register your models here.


class StuUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'pwd', 'e', 'col', 's', ]


class BookAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'title', 'author', 'press', 'pub_time', 'is_borrow']


class HisAdmin(admin.ModelAdmin):
    list_display = ['book', 'bor_time', 're_time', 'is_re', 'user', 'book', ]


admin.site.register(StuUser, StuUserAdmin)
admin.site.register(BookInfo, BookAdmin)
admin.site.register(History, HisAdmin)
admin.site.register(HotPic)
