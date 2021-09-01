from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Template)
admin.site.register(models.Document)
admin.site.register(models.Field)
admin.site.register(models.FieldType)
