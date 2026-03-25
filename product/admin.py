from django.contrib import admin
from . import models
# Register your models here.

# Регаем админ-меню
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Review)
