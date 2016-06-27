from django.contrib import admin

# Register your models here.
import models

admin.site.register(models.UserProfile)
admin.site.register(models.Item)
admin.site.register(models.Transaction)
admin.site.register(models.Supplier)