from django.contrib import admin
from malipo.models import Login, Finger_Print, Department, Employee, LeaveTable, Timeslot
# Register your models here.
admin.site.register(Login)
admin.site.register(Finger_Print)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(LeaveTable)
admin.site.register(Timeslot)
