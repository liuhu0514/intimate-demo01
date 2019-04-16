from django.contrib import admin
from .models import TeaInfo, ClassInfo, StuInfo

# Register your models here.


class ClassInfoInline(admin.StackedInline):
    model = ClassInfo
    # 关联个数
    extra = 1


class StuInfoInline(admin.StackedInline):
    model = StuInfo
    extra = 1


class TeaInfoAdmin(admin.ModelAdmin):
    # 显示字段，可以点击列头进行排序
    list_display = ['id1', 'skill', 'subject']
    # 过滤字段，过滤边框会出现在右侧
    list_filter = ['tname']
    # 搜索字段。搜索框会出现在上侧
    search_fields = ['tname', 'tsubject']
    # 分页，分页框会出现在下侧
    list_per_page = 5
    # 添加教师的时候可以额外 添加班级
    inlines = [ClassInfoInline]


class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ['id1', 'skill', 'tea']
    list_filter = ['cname']
    search_fields = ['cname']
    list_per_page = 5
    inlines = [StuInfoInline]


class StuInfoAdmin(admin.ModelAdmin):
    list_display = ['id1', 'skill', 'age', 'gender', 'sc']
    list_filter = ['sname']
    search_fields = ['sname', 'sage']
    list_per_page = 5


admin.site.register(TeaInfo, TeaInfoAdmin)
admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(StuInfo, StuInfoAdmin)
