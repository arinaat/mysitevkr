from django.contrib import admin
from .models import Post, Images
# Register your models here.

class ColorsInLine(admin.StackedInline):
    model = Images

@admin.register(Post)
class Posts(admin.ModelAdmin):
    inlines = [ColorsInLine, ]



