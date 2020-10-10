from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Login, Finger_Print, Department, Employee, LeaveTable, Timeslot


class loginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"


class fingerForm(forms.ModelForm):
    class Meta:
        model = Finger_Print
        fields = '__all__'


class deptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class employeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class lForm(forms.ModelForm):
    class Meta:
        model = LeaveTable
        fields = '__all__'

        widgets = {
            # default date-format %m/%d/%Y will be used
            'leave_Start_Date': DatePickerInput(),
            # specify date-frmat
            'leave_End_Date': DatePickerInput(format='%Y-%m-%d'),
        }


class timeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = '__all__'
