from django.contrib import admin
from .models import author, category,article,comment

# Register your models here.
class authorModel(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        Model =author
class categoryModel(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        Model = category

class articleModel(admin.ModelAdmin):
    list_display = ['article_author','title','body','posted_on','updated_on']
    class Meta:
        Model = article

class commentModel(admin.ModelAdmin):
    list_display = ['__str__']
    class Meta:
        Model =comment



admin.site.register(comment,commentModel)
admin.site.register(author,authorModel)
admin.site.register(category,categoryModel)
admin.site.register(article,articleModel)