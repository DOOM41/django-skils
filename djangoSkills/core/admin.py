from django.contrib import admin
from core.models import Article,Comment,OtherImage

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(OtherImage)