from django.contrib import admin
from .models import Service 

class AdminService(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') 

admin.site.register(Service, AdminService)
