from django.contrib import admin

from .models import *
# Register your models here.


class GaleriImageInline(admin.TabularInline):
    model = GaleriImage
    extra = 1


class GaleriImageAdmin(admin.ModelAdmin):
    
    list_display = ('title',)

    ordering = ('-title',)

    inlines = [
        GaleriImageInline,
    ]


admin.site.register(GaleriModel, GaleriImageAdmin)


admin.site.register(GaleriAnasayfaModel)



