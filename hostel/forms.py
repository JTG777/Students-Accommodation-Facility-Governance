from django import forms
from .models import RoomAssign,Room
from baseapp.models import Student
from django.db.models import F


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
        assigned_rooms=Room.objects.filter(room_max_capacity=F('room_alloted'))
        # assigned_rooms = RoomAssign.objects.all().values_list('room', flat=True)
        assigned_students = RoomAssign.objects.all().values_list('student', flat=True)

        self.fields['room'].queryset = Room.objects.exclude(pk__in=assigned_rooms)
        self.fields['student'].queryset = Student.objects.exclude(pk__in=assigned_students)

    def save(self,commit,*args,**kwargs,):
        room_assign=super().save(commit=False)
        if room_assign.room.room_type=='Triple' and room_assign.room.room_max_capacity!=room_assign.room.room_alloted:
            room_assign.room.room_alloted+=1
        if room_assign.room.room_type=='Double' and room_assign.room.room_max_capacity!=room_assign.room.room_alloted:
            room_assign.room.room_alloted+=1
        else:
            room_assign.room.room_alloted=1
        room_assign.room.save()    
        return room_assign
