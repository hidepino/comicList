from django.contrib import admin
from cms.models import Comic

# Register your models here.
# admin.site.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'main_title', 'home_link',)  # 一覧に出したい項目
    list_display_links = ('title', 'link', 'main_title', 'home_link',)  # 修正リンクでクリックできる項目


admin.site.register(Comic, ComicAdmin)
