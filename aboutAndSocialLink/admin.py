from django.contrib import admin
from .models import About,SocialLink
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count  = About.objects.all().count()
        if count == 0:
            return True
        else:
            return False

class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform','link','created_at','updated_at')

admin.site.register(About,AboutAdmin)
admin.site.register(SocialLink,SocialLinkAdmin)