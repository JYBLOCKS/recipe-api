from django.contrib import admin
from recipe.models import Category, Instruction, Recipe

# Register your models here.
admin.site.register(Category)
admin.site.register(Instruction)
admin.site.register(Recipe)