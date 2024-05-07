from django.contrib import admin
from .models import *

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display=['id','filmismi','kategori']
    # list_display_links=['filmismi']
    list_filter=['kategori']
    # list_per_page=1
    search_fields=['filmismi','kategori__name']
    list_editable=['filmismi']


admin.site.register(Movies,MoviesAdmin)
admin.site.register(Kategori)
admin.site.register(Tur)



