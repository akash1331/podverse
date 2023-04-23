from django.contrib import admin

from .models import *

# Register your models here.

# class podcastAdminSite(admin.ModelAdmin):
#     list_display = ('podname','podcreator','liked','poddata','genre')

# class GenreAdminSite(admin.ModelAdmin):
#     list_display = ('genrepod')

admin.site.register(Genre)
admin.site.register(podcastDetails)
admin.site.register(typeofPod)
admin.site.register(playlist)
admin.site.register(Language)
admin.site.site_header = 'Podverse Backend'