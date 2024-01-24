from django.contrib import admin

from blango_auth.models import User
from blango_auth.admin import BlangoUserAdmin
from blog.models import Tag, Post, Comment, AuthorProfile

# Register your models here.

admin.site.register(User, BlangoUserAdmin)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ["title", "slug", "published_at"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(AuthorProfile)
