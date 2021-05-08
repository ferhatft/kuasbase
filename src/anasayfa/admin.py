from django.contrib import admin

from .models import *
# Register your models here.

class İnspectImageInline(admin.TabularInline):
    model = İnspectImage
    extra = 1
    

class İnspectImageAdmin(admin.ModelAdmin):
    inlines = [ İnspectImageInline ]
    
    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(İnspectModel, İnspectImageAdmin)



class ReferansImageInline(admin.TabularInline):
    model = ReferansImage
    extra = 1

class İnspectImageAdmin(admin.ModelAdmin):
    inlines = [ ReferansImageInline, ]
    

admin.site.register(ReferansModel, İnspectImageAdmin)




admin.site.register(WhatwedoModel)
admin.site.register(WhoweareModel)

admin.site.register(KuasLogoModel)


