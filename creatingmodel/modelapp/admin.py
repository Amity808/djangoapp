from django.contrib import admin
from modelapp.models import Empolyee
# Register your models here.

class EmployeAdmin(admin.ModelAdmin):
    list_display=['firstname', 'lastname']


admin.site.register(Empolyee,EmployeAdmin)