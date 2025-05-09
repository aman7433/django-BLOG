from django.contrib import admin
from .models import category , comment, post    
# Register your models here.
class category_admin(admin.ModelAdmin):
    pass
class comment_admin(admin.ModelAdmin):
    pass
class post_admin(admin.ModelAdmin):
    pass
 
admin.site.register(category,category_admin)
admin.site.register(comment,comment_admin)
admin.site.register(post,post_admin)