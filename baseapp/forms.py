from .models import Student
from django import forms
from .models import RoomAssign
from .models import Room
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentregisterForm(forms.ModelForm):
    class Meta:
        model=Student
        # fields='__all__'
        exclude=['user']
        widgets = {
            'gender': forms.RadioSelect(),
            'student_dob': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
}

class RoomAssignForm(forms.ModelForm):
    class Meta:
        model=RoomAssign
        exclude=['total_payment']

        widgets = {
            'room_assigned_date': forms.DateInput(attrs={'format': 'yyyy-mm-dd','type':'date'}),
            
        }

    def __init__(self, *args, **kwargs):
        super(RoomAssignForm, self).__init__(*args, **kwargs)

        # Filter available rooms and students
        assigned_rooms = RoomAssign.objects.all().values_list('room', flat=True)
        assigned_students = RoomAssign.objects.all().values_list('student', flat=True)

        self.fields['room'].queryset = Room.objects.exclude(pk__in=assigned_rooms)
        self.fields['student'].queryset = Student.objects.exclude(pk__in=assigned_students)

class Userform(UserCreationForm):
    class meta:
        model=User
        fields=['username','password1','password2']



        