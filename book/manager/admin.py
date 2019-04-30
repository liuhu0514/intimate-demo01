from django.contrib import admin
from .models import Manager, Article

# Register your models here.


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'password', ]


admin.site.register(Manager)
admin.site.register(Article)
