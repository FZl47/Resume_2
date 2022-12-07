from django.contrib import admin
from . import models

admin.site.register(models.Information)
admin.site.register(models.Certificate)
admin.site.register(models.Review)
admin.site.register(models.Contact)
admin.site.register(models.Gallery)
admin.site.register(models.Image)
admin.site.register(models.WorkSample)
admin.site.register(models.Skill)
admin.site.register(models.TelegramBot)
admin.site.register(models.MessageNotif)