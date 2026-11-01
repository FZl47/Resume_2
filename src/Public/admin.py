from django.contrib import admin
from . import models


class ImageInline(admin.TabularInline):
    model = models.Image
    extra = 1
    fields = ('image', 'order')
    ordering = ('order', 'id')


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'gallery', 'order')
    list_editable = ('order',)
    list_filter = ('gallery',)
    ordering = ('gallery', 'order', 'id')


@admin.register(models.WorkSample)
class WorkSampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'date_time_create', 'views')
    list_editable = ('order',)
    ordering = ('order', '-id')


admin.site.register(models.Information)
admin.site.register(models.Certificate)
admin.site.register(models.Review)
admin.site.register(models.Contact)
admin.site.register(models.Category)
admin.site.register(models.Skill)
admin.site.register(models.Experience)
admin.site.register(models.ExperienceSkill)
admin.site.register(models.Education)
admin.site.register(models.TelegramBot)
admin.site.register(models.MessageNotif)
