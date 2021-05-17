from django.contrib import admin
from blogApp.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','body','created','publish','updated','status']
    prepopulated_fields={'slug':('title',)}
    list_filter= ('title','author','created','publish')
    search_fields=('title','body',)
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']



admin.site.register(Post,PostAdmin)