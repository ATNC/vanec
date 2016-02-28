from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import Client, Documents

# class ClientAdmin(admin.StackedInline):
#     model = Client

class DocumentsAdmin(admin.StackedInline):
    model = Documents
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    inlines = (DocumentsAdmin, )

# admin.site.unregister(User)
admin.site.register(Client, ClientAdmin)
# Register your models here.
