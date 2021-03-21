from django.contrib import admin
from .models import Developer,CustomUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Developer)
