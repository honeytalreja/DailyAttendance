from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Site)
admin.site.register(Zone)
admin.site.register(Home)
admin.site.register(Shift)
admin.site.register(AttendanceRecord)
