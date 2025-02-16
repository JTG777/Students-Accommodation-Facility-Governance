from django.db import models
from baseapp.models import OneteamBranch,Student
from django.utils.timezone import now

# Create your models here.
class Warden(models.Model):  # Caretaker Model
    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=15,)

    def __str__(self):
        return self.name
    

    

class Hostel(models.Model):
    HOSTEL_TYPE=(("Men's Hostel","Men's Hostel"),("Women's Hostel","Women's Hostel"))
    hostel_type=models.CharField(max_length=30,choices=HOSTEL_TYPE)
    warden=models.OneToOneField(Warden,on_delete=models.SET_NULL,null=True)
    branch=models.ForeignKey(OneteamBranch,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.hostel_type} of {self.branch} '

class RoomFeeStructure(models.Model):
    ROOM_TYPE=(('Single','Single'),('Double','Double'),('Triple','Triple'))

    room_type=models.CharField(choices=ROOM_TYPE,max_length=20)
    fee_per_person=models.DecimalField(max_digits=10, decimal_places=2,default=2000)

    def __str__(self):
        return f" Rs.{self.fee_per_person} per person for a {self.room_type} Bed Room "
    


class Room(models.Model):
    # room_name=models.CharField(max_length=30,default=None)
    ROOM_TYPE=(('Single','Single'),('Double','Double'),('Triple','Triple'))
    room_no=models.IntegerField(unique=True)
    room_type=models.CharField(max_length=20,choices=ROOM_TYPE,)
    hostel=models.ForeignKey(Hostel,on_delete=models.CASCADE,default=None)
    room_max_capacity=models.IntegerField(default=1)
    room_alloted=models.IntegerField(default=0)
    room_fee=models.ForeignKey(RoomFeeStructure,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"Room no. {self.room_no}, {self.room_type} Bed room in {self.hostel}  "
    

class FeesMethod(models.Model):
    TYPE=(('ONE TIME','One Time Payment'),('RECURRING','Recurring Payment'))

    fees_type=models.CharField(choices=TYPE,max_length=50)

    def __str__(self):
        return self.fees_type


class RoomAssign(models.Model):
    FOOD=((True,'Yes'),(False,'No'))
    room=models.ForeignKey(Room,on_delete=models.CASCADE,null=True,blank=True,related_name='assigned')
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    Duration=models.IntegerField(default=1,help_text="In months")
    room_assigned_date=models.DateField(default=now)
    food_required=models.BooleanField(max_length=20,choices=FOOD,default=False,help_text='2000 rs for one month')
    fees_type=models.ForeignKey(FeesMethod,on_delete=models.CASCADE,null=True,help_text='hostel fee 4000rs per month ,for recurring payment,there will be 3 installments that you have to pay in each month')
    # total_payment=models.DecimalField(max_digits=10, decimal_places=2)
    dated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    

    def __str__(self):
        return f"{self.student} assigned in {self.room.room_type} Bed of Room {self.room.room_no} of {self.room.hostel.hostel_type} in {self.room.hostel.branch}"
    
    


class Payment(models.Model):
    room_assigned=models.OneToOneField(RoomAssign,on_delete=models.SET_NULL,null=True)
    is_paid=models.BooleanField(default=False)
    food_charge=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    fees_type=models.CharField(max_length=50,default='ONE TIME')
    amount_paid=models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pending_amount=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_payment=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    payment_date=models.DateTimeField(blank=True,null=True)
    next_due_date=models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    recurring_installments=models.IntegerField(blank=True,null=True)
    

    def save(self,*args,**kwargs):
        if self.total_payment is not None:
            self.pending_amount=max(self.total_payment-self.amount_paid,0)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.total_payment} for {self.room_assigned}"

class RecurringPayment(models.Model):
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    amount_due=models.DecimalField(max_digits=10,decimal_places=2)
    due_date=models.DateField()
    is_paid=models.BooleanField(default=False)
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return f"Installment of {self.amount_due} due on {self.due_date}"

# class Onetimepayment(models.Model):
#     room_assign = models.ForeignKey(RoomAssign,on_delete=models.CASCADE) 
#     is_paid=models.BooleanField(default=False)
#     amount=models.DecimalField(max_digits=10, decimal_places=2)  
#     payment_date=models.DateField()