from django.contrib import admin
from .models import Author, Tag, Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
