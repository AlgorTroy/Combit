from django.contrib import admin
from .models import Category, Job, Application, Interest

admin.site.register([Application, Interest])

class JobAdmin(admin.ModelAdmin):
    search_fields = ('title', 'details', 'tags')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Job, JobAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
