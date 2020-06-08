from django.contrib import admin
from .models import Webnote, Craft, Status, Access, Tool, Pattern, Yarn


@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'size', 'producer', 'type', 'material')


@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'image', 'scheme', 'description', 'source')


@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'color_lot', 'weight', 'length', 'label', 'source')


@admin.register(Webnote)
class WebnoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'user', 'create_date', 'for_who', 'craft', 'status', 'access')
