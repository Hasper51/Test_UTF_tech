from django.contrib import admin

from menu.models import FoodCategory, Food


# Register your models here.

admin.site.register(FoodCategory)
admin.site.register(Food)