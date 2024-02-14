from django.contrib import admin
from .models import *
from mptt.admin import DraggableMPTTAdmin

class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions','indented_title')
    list_display_links = ('indented_title',)
    # ordering = ('pk',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(ProductImage)
admin.site.register(Brand)

# Продукты
#     Конфеты
#         Шоколат
#             Бренды: 3 штуки
#             Товары: 5-9 штук