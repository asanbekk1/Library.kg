from django.contrib import admin
from . import models

admin.site.register(models.BookModel)
admin.site.register(models.Comment)