from django.contrib import admin

# Register your models here.
from .models import Guitar, Owner
admin.site.register(Guitar)
admin.site.register(Owner)

