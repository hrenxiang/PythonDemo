from django.contrib import admin

from api.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')  # 指定要显示的字段
    search_fields = ('title', 'content')  # 添加搜索功能
    list_filter = ('created_at',)  # 添加过滤功能
    ordering = ('-created_at',)  # 按创建时间排序


# Register your models here.
admin.site.register(Article, ArticleAdmin)
