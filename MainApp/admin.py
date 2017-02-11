from django.contrib import admin
from .models import Tile
# Register your models here.


class TileAdmin(admin.ModelAdmin):
    list_display = ('title', 'open_jobs', 'posted_by')


admin.site.register(Tile, TileAdmin)
