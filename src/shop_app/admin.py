from django.contrib import admin

from . import models


# Register your models here.

admin.site.register(models.Reference_book)
admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Publishing_house)

