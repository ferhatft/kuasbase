from django.contrib import admin

from .models import *


class BlogonlyImageInline(admin.TabularInline):
    model = BlogonlyImage
    extra = 1


class BlogImageAdmin(admin.ModelAdmin):
    inlines = [BlogonlyImageInline,]


admin.site.register(BlogModel, BlogImageAdmin)