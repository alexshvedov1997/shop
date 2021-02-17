from django.contrib import admin
from .models import Category, Product
from django.utils.html import mark_safe

# Register your models here.

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug')
    prepopulated_fields = {'slug':('name', )}
    list_display_links = ("name","id")

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "slug","available",
                    "created", "updated", "get_image", "category")
    search_fields = ("name", "category__name")
    list_filter = ("category",)
    prepopulated_fields = {'slug':('name',)}
    save_on_top =  True
    list_editable = ("available",)

    def get_image(self, obj):
        if(obj.product_image):
            return mark_safe("<img src = '{}' width = '50' />".format(obj.product_image.url))
        return  None

    get_image.__name__ = "Изображение"


