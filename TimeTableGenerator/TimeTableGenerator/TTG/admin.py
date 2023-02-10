from django.contrib import admin
from .models import Subject, Room, Batch, Time
# Register your models here.

admin.site.register(Subject)
admin.site.register(Room)
admin.site.register(Batch)
admin.site.register(Time)