from django.contrib import admin
from .models import Category , Comment, Post    
# Register your models here.
class category_admin(admin.ModelAdmin):
    pass
class comment_admin(admin.ModelAdmin):
    pass
class post_admin(admin.ModelAdmin):
    pass
 
admin.site.register(Category,category_admin)
admin.site.register(Comment,comment_admin)
admin.site.register(Post,post_admin)