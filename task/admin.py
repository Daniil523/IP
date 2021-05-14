from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import Item, Category, Status, Label, Project, Time
from import_export.admin import ImportExportModelAdmin


class ItemInline(admin.TabularInline):
    model = Item


class TimeAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ('start', 'endPoint', 'endFact')
    actions = ["setStart"]

    def setStart(self, request, queryset):
        row_update = queryset.update(start="00:00:00")

    setStart.short_description = "Обнулить начало"


class ItemResource(resources.ModelResource):
    status = fields.Field(column_name='status', attribute='status', widget=ForeignKeyWidget(Status, 'name'))

    class Meta:
        model = Item


class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource
    search_fields = ('name',)
    list_display = ('name', 'category', 'status')
    list_filter = ('category',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Label)
admin.site.register(Project)
admin.site.register(Time, TimeAdmin)
