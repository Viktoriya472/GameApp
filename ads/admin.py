from django.contrib import admin
from ads.models import Ad, Game, Comment


class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content_upload')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'active')
    list_display_links = ('id', 'text')
    search_fields = ('text',)


admin.site.register(Ad, AdAdmin)
admin.site.register(Game)
admin.site.register(Comment, CommentAdmin)
