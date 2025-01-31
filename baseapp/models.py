from django.db import models
from django.contrib.auth.models import User

class Master(models.Model):

    isactive = models.BooleanField(default=True, verbose_name="Active")

    class Meta:
        abstract = True



# Create your models here.
class OneteamBranch(Master):
    branch_name=models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "OneTeam Branches"

    def __str__(self):
        return self.branch_name



class Course(models.Model):
    course_name=models.CharField(max_length=40)
    

    def __str__(self):
        return self.course_name

class Trainer(models.Model):
    trainer_name=models.CharField(max_length=40)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    branch=models.ForeignKey(OneteamBranch,on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.trainer_name} teach {self.course.course_name}"
    




class Student(models.Model):
    GENDER=(("Male","Male"),("Female","Female"))

    student_name=models.CharField(max_length=40)
    student_dob=models.DateField(help_text="Write date of birth in yyyy-mm-dd format")
    student_no=models.BigIntegerField(unique=True)
    student_email_id=models.EmailField(unique=True,default=None)
    gender=models.CharField(max_length=6,choices=GENDER,default=None)
    guardian_name=models.CharField(max_length=40)
    guardian_no=models.BigIntegerField(unique=True)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    oneteam_branch_name=models.ForeignKey(OneteamBranch,on_delete=models.CASCADE, limit_choices_to={"isactive":True})
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    


    

    def __str__(self):
        return self.student_name
    


    

    

class Hostel(models.Model):
    hostel_type=models.CharField(max_length=30,default=None)
    caretaker=models.CharField(max_length=40,default=None)

    def __str__(self):
        return f'{self.hostel_type}'


class Room(models.Model):
    room_name=models.CharField(max_length=30,default=None)
    ROOM_TYPE=(('Single','Single'),('Double','Double'),('Triple','Triple'))
    room_no=models.IntegerField()
    room_type=models.CharField(max_length=20,choices=ROOM_TYPE,)
    hostel=models.ForeignKey(Hostel,on_delete=models.CASCADE,default=None)
    # room_capacity=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.room_name}, {self.hostel} {self.room_type} Bed room"
    

class Fees(models.Model):
    fees_type=models.CharField(default=None,max_length=50)

    def __str__(self):
        return self.fees_type


class RoomAssign(models.Model):
    FOOD=((True,'Yes'),(False,'No'))
    room=models.OneToOneField(Room,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    Duration=models.IntegerField(default=None,help_text="In months")
    room_assigned_date=models.DateField(default=None)
    food_required=models.BooleanField(max_length=20,choices=FOOD,default=None,help_text='2000 rs for one month')
    fees_type=models.ForeignKey(Fees,on_delete=models.CASCADE,default=None,help_text='hostel fee 4000rs per month ,for recurring payment,there will be 3 installments that you have to pay in each month')
    total_payment=models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.room.room_name
    

class Onetimepayment(models.Model):
    room_assign = models.ForeignKey(RoomAssign,on_delete=models.CASCADE) 
    is_paid=models.BooleanField(default=False)
    amount=models.DecimalField(max_digits=10, decimal_places=2)  
    payment_date=models.DateField() 




