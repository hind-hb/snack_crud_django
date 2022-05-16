from django.contrib import admin
from snacks.models import Snacks
# Register your models here.
@admin.register(Snacks)
class AdminSnack(admin.ModelAdmin):
    list_display = ['id', 'title', 'purchaser', 'description']
    search_fields = ('title', )
